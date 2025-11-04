#!/usr/bin/env python3
# 文字列処理 (正規表現) のサンプル

import re  # 正規表現を扱うライブラリ


def main():
    text = "2018 (MMXVIII) was a common year starting on Monday of the Gregorian calendar, the 2018th year of the Common Era (CE) and Anno Domini (AD) designations, the 18th year of the 3rd millennium, the 18th year of the 21st century, and the 9th year of the 2010s decade."

    # re.findall(): パターンにマッチする全ての文字列を抽出
    print("1. アラビア数字を全て抽出:")
    liresult = re.findall(r"\d+", text)  # \d+ は1つ以上の数字
    print(liresult)

    # 大文字から始まる単語を抽出
    print("\n2. 大文字から始まる単語を抽出:")
    liresult = re.findall(r"[A-Z][a-z]+", text)
    print(liresult)

    # re.search(): パターンにマッチする最初の文字列を検索
    print("\n3. 文の最初が数字かどうかを判定:")
    if re.search(r"^\d", text):  # ^ は文字列の先頭
        print("Yes, 文の最初は数字です")
    else:
        print("No, 文の最初は数字ではありません")

    # re.sub(): パターンにマッチする文字列を置換
    print("\n4. 括弧で囲まれた部分を削除:")
    replaced_text = re.sub(r"\(\w+\)\s", "", text)  # \( と \) はエスケープが必要
    print(replaced_text)

    # re.split(): パターンで文字列を分割
    print("\n5. 空白で文字列を分割:")
    liresult = re.split(r"\s+", text)  # \s+ は1つ以上の空白文字
    print(f"単語数: {len(liresult)}")
    print(f"最初の5単語: {liresult[:5]}")

    # その他の正規表現パターンの例
    print("\n6. その他のパターン例:")
    test_strings = [
        "hello@example.com",
        "test123@test.co.jp",
        "not-an-email"
    ]

    # メールアドレスの簡易パターン
    email_pattern = r"\w+@\w+\.\w+"

    print("メールアドレスの判定:")
    for s in test_strings:
        if re.match(email_pattern, s):
            print(f"  {s} -> メールアドレスです")
        else:
            print(f"  {s} -> メールアドレスではありません")

    # 正規表現の特殊文字の説明
    print("\n7. 正規表現の主な特殊文字:")
    print("  \\d : 数字 (0-9)")
    print("  \\w : 単語文字 (英数字とアンダースコア)")
    print("  \\s : 空白文字 (スペース、タブ、改行など)")
    print("  +  : 直前のパターンの1回以上の繰り返し")
    print("  *  : 直前のパターンの0回以上の繰り返し")
    print("  ^  : 文字列の先頭")
    print("  $  : 文字列の末尾")
    print("  .  : 任意の1文字")
    print("  [] : 文字クラス (例: [A-Z]は大文字アルファベット)")


if __name__ == "__main__":
    main()
