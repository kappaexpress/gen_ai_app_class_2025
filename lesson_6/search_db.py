"""
rag_database.dbを検索するスクリプト
"""

from simple_doc_search import SimpleDocumentSearch


if __name__ == "__main__":
    # ファイルパス
    db_path = "rag_database.db"

    # SimpleDocumentSearchインスタンスを作成
    print(f"データベース '{db_path}' を読み込んでいます...")
    search_engine = SimpleDocumentSearch(db_path=db_path, n=2)

    query = "明智は誰ですか？"
    results = search_engine.search(query)

    for id, content, score in results:
        print(f"ID: {id}, スコア: {score}")
        print(content)

    # データベース接続を閉じる
    search_engine.close()