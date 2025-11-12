"""
text.xlsxからSimpleDocumentSearchを使ってRAGデータベースを作成するスクリプト
"""

from simple_doc_search import SimpleDocumentSearch
import os

if __name__ == "__main__":
    # ファイルパス
    excel_path = "text.xlsx"
    db_path = "rag_database.db"

    # 既存のDBがあれば削除（新規作成する場合）
    if os.path.exists(db_path):
        print(f"既存のデータベース {db_path} を削除します...")
        os.remove(db_path)

    # SimpleDocumentSearchインスタンスを作成（3-gramを使用）
    print("データベースを初期化しています...")
    search_engine = SimpleDocumentSearch(db_path=db_path, n=2)

    # エクセルファイルから文書をインポート
    print(f"\n{excel_path} からデータをインポートしています...")
    search_engine.import_from_excel(
        excel_path=excel_path,
        doc_column='doc',  # 文書内容が含まれる列名
        metadata_columns=['index']  # メタデータとして保存する列名
    )

    # 統計情報を表示
    stats = search_engine.get_stats()
    print(f"\n=== データベース作成完了 ===")
    print(f"総文書数: {stats['total_documents']}")
    print(f"ユニークなn-gram数: {stats['unique_ngrams']}")
    print(f"データベースファイル: {db_path}")

    # テスト検索を実行
    print("\n=== テスト検索 ===")
    test_query = "明智探偵は誰ですか？"
    print(f"検索クエリ: {test_query}")
    results = search_engine.search(test_query, top_k=3)

    for i, (doc_id, content, score) in enumerate(results):
        print(f"\n結果 {i+1} (ID: {doc_id}, スコア: {score:.3f})")
        # 長い文書の場合は最初の100文字だけ表示
        preview = content[:100] + "..." if len(content) > 100 else content
        print(f"内容: {preview}")

    # データベース接続を閉じる
    search_engine.close()
    print("\n✓ 完了しました")
