#!/usr/bin/env python3
# 繰り返し処理 (for) のサンプル

def main():
    # rangeを使った繰り返し
    print("range(5)を使った繰り返し:")
    for i in range(5):
        print(i)
    print("hoge")  # 繰り返しの外 (アウトデント)

    # リストの各要素にアクセス
    print("\nリストの各要素にアクセス:")
    list_a = [10, 4, "aaa"]
    for w in list_a:
        print(w)

    # ディクショナリのキーと値にアクセス
    print("\nディクショナリのキーと値にアクセス:")
    dict_a = {"January": "1", "February": "2"}
    for k in dict_a.keys():  # dict_a.keys()でキーのリストを取得
        print(k, dict_a[k])

    # items()を使ったディクショナリの繰り返し
    print("\nitems()を使った繰り返し:")
    for k, v in dict_a.items():
        print(f"{k} corresponds to {v}")

    # enumerate()を使ってインデックスと値を同時に取得
    print("\nenumerate()を使った繰り返し:")
    fruits = ["apple", "banana", "cherry"]
    for index, fruit in enumerate(fruits):
        print(f"{index}: {fruit}")

if __name__ == "__main__":
    main()
