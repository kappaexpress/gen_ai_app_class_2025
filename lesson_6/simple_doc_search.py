"""
簡易文書検索システム - SQLiteとn-gramベースの類似度検索
"""

import sqlite3
import re
from collections import Counter
from typing import List, Tuple, Dict
import json
import pandas as pd


class SimpleDocumentSearch:
    def __init__(self, db_path: str = "rag_database.db", n: int = 3):
        """
        Args:
            db_path: SQLiteデータベースのパス
            n: n-gramのn（デフォルトは3-gram）
        """
        self.db_path = db_path
        self.n = n
        self.conn = sqlite3.connect(db_path)
        self._initialize_db()
    
    def _initialize_db(self):
        """データベースの初期化"""
        cursor = self.conn.cursor()
        
        # 文書チャンクを保存するテーブル
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                metadata TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # n-gramを保存するテーブル
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ngrams (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                document_id INTEGER NOT NULL,
                ngram TEXT NOT NULL,
                frequency INTEGER NOT NULL,
                FOREIGN KEY (document_id) REFERENCES documents(id)
            )
        """)
        
        # インデックスを作成
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_ngrams 
            ON ngrams(ngram)
        """)
        
        self.conn.commit()
    
    def _extract_ngrams(self, text: str) -> Counter:
        """
        テキストからn-gramを抽出
        
        Args:
            text: 入力テキスト
            
        Returns:
            n-gramとその出現頻度のCounter
        """
        # 正規化（小文字化、記号削除）
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        
        # 文字レベルのn-gram
        ngrams = []
        for i in range(len(text) - self.n + 1):
            ngram = text[i:i + self.n]
            if ngram.strip():  # 空白のみのn-gramを除外
                ngrams.append(ngram)
        
        return Counter(ngrams)
    
    def add_document(self, content: str, metadata: Dict = None):
        """
        文書をデータベースに追加
        
        Args:
            content: 文書の内容
            metadata: メタデータ（辞書形式）
        """
        cursor = self.conn.cursor()
        
        # 文書を保存
        metadata_json = json.dumps(metadata) if metadata else None
        cursor.execute(
            "INSERT INTO documents (content, metadata) VALUES (?, ?)",
            (content, metadata_json)
        )
        doc_id = cursor.lastrowid
        
        # n-gramを抽出して保存
        ngrams = self._extract_ngrams(content)
        for ngram, freq in ngrams.items():
            cursor.execute(
                "INSERT INTO ngrams (document_id, ngram, frequency) VALUES (?, ?, ?)",
                (doc_id, ngram, freq)
            )
        
        self.conn.commit()
        print(f"文書ID {doc_id} を追加しました")
    
    def add_documents_batch(self, documents: List[str]):
        """
        複数の文書を一括追加

        Args:
            documents: 文書のリスト
        """
        for doc in documents:
            self.add_document(doc)

    def import_from_excel(self, excel_path: str, doc_column: str = 'doc',
                         metadata_columns: List[str] = None):
        """
        エクセルファイルから文書をインポート

        Args:
            excel_path: エクセルファイルのパス
            doc_column: 文書内容が含まれる列名（デフォルト: 'doc'）
            metadata_columns: メタデータとして保存する列名のリスト
        """
        try:
            # エクセルファイルを読み込み
            df = pd.read_excel(excel_path)

            # doc_columnが存在するか確認
            if doc_column not in df.columns:
                raise ValueError(f"列 '{doc_column}' がエクセルファイルに存在しません")

            print(f"エクセルファイルから{len(df)}件の文書を読み込んでいます...")

            # 各行を処理
            for _, row in df.iterrows():
                content = str(row[doc_column])

                # メタデータを収集
                metadata = {}
                if metadata_columns:
                    for col in metadata_columns:
                        if col in df.columns:
                            metadata[col] = row[col]
                else:
                    # 全ての列（doc_column以外）をメタデータとして保存
                    for col in df.columns:
                        if col != doc_column:
                            metadata[col] = row[col]

                # 文書を追加
                self.add_document(content, metadata)

            print(f"✓ {len(df)}件の文書をインポートしました")

        except Exception as e:
            print(f"エラー: エクセルファイルの読み込みに失敗しました - {e}")
    
    def _calculate_similarity(self, query_ngrams: Counter, doc_ngrams: Counter) -> float:
        """
        Jaccard係数を使って類似度を計算
        
        Args:
            query_ngrams: クエリのn-gram
            doc_ngrams: 文書のn-gram
            
        Returns:
            類似度スコア（0.0～1.0）
        """
        # n-gramの集合を作成
        query_set = set(query_ngrams.keys())
        doc_set = set(doc_ngrams.keys())
        
        # Jaccard係数
        if not query_set or not doc_set:
            return 0.0
        
        intersection = len(query_set & doc_set)
        union = len(query_set | doc_set)
        
        return intersection / union if union > 0 else 0.0
    
    def search(self, query: str, top_k: int = 3) -> List[Tuple[int, str, float]]:
        """
        クエリに類似した文書を検索
        
        Args:
            query: 検索クエリ
            top_k: 返す文書の数
            
        Returns:
            (文書ID, 文書内容, 類似度スコア)のリスト
        """
        # クエリからn-gramを抽出
        query_ngrams = self._extract_ngrams(query)
        
        if not query_ngrams:
            return []
        
        # クエリのn-gramに一致する文書を取得
        cursor = self.conn.cursor()
        query_ngram_list = list(query_ngrams.keys())
        placeholders = ','.join(['?'] * len(query_ngram_list))
        
        cursor.execute(f"""
            SELECT DISTINCT d.id, d.content
            FROM documents d
            JOIN ngrams n ON d.id = n.document_id
            WHERE n.ngram IN ({placeholders})
        """, query_ngram_list)
        
        candidates = cursor.fetchall()
        
        # 各候補文書の類似度を計算
        results = []
        for doc_id, content in candidates:
            # 文書のn-gramを取得
            cursor.execute("""
                SELECT ngram, frequency
                FROM ngrams
                WHERE document_id = ?
            """, (doc_id,))
            
            doc_ngrams = Counter(dict(cursor.fetchall()))
            
            # 類似度計算
            similarity = self._calculate_similarity(query_ngrams, doc_ngrams)
            results.append((doc_id, content, similarity))
        
        # 類似度でソート
        results.sort(key=lambda x: x[2], reverse=True)
        
        return results[:top_k]

    def get_stats(self) -> Dict:
        """データベースの統計情報を取得"""
        cursor = self.conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM documents")
        doc_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(DISTINCT ngram) FROM ngrams")
        unique_ngrams = cursor.fetchone()[0]
        
        return {
            "total_documents": doc_count,
            "unique_ngrams": unique_ngrams
        }
    
    def close(self):
        """データベース接続を閉じる"""
        self.conn.close()


# 使用例
if __name__ == "__main__":
    # 文書検索システムを初期化（3-gramを使用）
    search_engine = SimpleDocumentSearch(n=3, db_path="sample.db")
    
    # サンプル文書を追加
    documents = [
        "Pythonは汎用的なプログラミング言語です。機械学習やWeb開発に広く使われています。",
        "SQLiteは軽量なリレーショナルデータベースです。サーバーレスで動作し、組み込みアプリケーションに適しています。",
        "機械学習は人工知能の一分野です。データからパターンを学習してタスクを実行します。",
        "Webアプリケーション開発には様々なフレームワークがあります。FlaskやDjangoが人気です。",
        "自然言語処理はテキストデータを扱う技術です。感情分析や機械翻訳などに応用されます。"
    ]
    
    print("文書を追加中...")
    search_engine.add_documents_batch(documents)

    # 統計情報を表示
    stats = search_engine.get_stats()
    print(f"\n統計情報: {stats}")
    
    # 検索テスト
    print("\n" + "="*50)
    queries = [
        "Pythonでの機械学習について",
        "データベースの種類",
        "自然言語処理の応用"
    ]
    
    for query in queries:
        print(f"\n検索クエリ: {query}")
        print("-" * 50)
        results = search_engine.search(query, top_k=2)
        
        for i, (doc_id, content, score) in enumerate(results):
            print(f"\n結果 {i+1} (ID: {doc_id}, スコア: {score:.3f})")
            print(f"内容: {content}")

    # クリーンアップ
    search_engine.close()