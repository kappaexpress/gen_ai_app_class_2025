#!/usr/bin/env python3
# リストとディクショナリのサンプル

def main():
    # リスト (list) の基本操作
    list_a = [10, 4, "aaa"]  # 数値と文字列を混在できる
    print("リストの要素にアクセス:")
    print(list_a[0])  # 最初の要素 (インデックスは0から始まる)
    print(list_a[1])  # 2番目の要素
    print(list_a[2])  # 3番目の要素

    # リストの長さを取得
    print(f"\nリストの長さ: {len(list_a)}")

    # リストに要素を追加
    list_a.append("new_element")
    print(f"追加後のリスト: {list_a}")

    # ディクショナリ (dictionary) の基本操作
    dict_a = {"January": "1", "February": "2", "March": "3"}
    print("\nディクショナリの要素にアクセス:")
    print(dict_a["January"])  # キーを指定して値を取得
    print(dict_a["February"])

    # ディクショナリに新しいキーと値を追加
    dict_a["April"] = "4"
    print(f"追加後のディクショナリ: {dict_a}")

    # キーが存在するか確認
    if "January" in dict_a:
        print("\nJanuaryはディクショナリに存在します")

if __name__ == "__main__":
    main()
