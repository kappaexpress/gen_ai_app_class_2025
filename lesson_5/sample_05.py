#!/usr/bin/env python3
# 繰り返し処理 (while) のサンプル

def main():
    # whileを使った繰り返し (条件がTrueの間繰り返す)
    print("whileを使った繰り返し (i < 10):")
    i = 0
    while i < 10:
        print(i)
        i = i + 1  # iをインクリメント (1ずつ増やす)

    # 不等号 != を使った繰り返し
    print("\n!= を使った繰り返し:")
    i = 0
    while i != 10:
        print(i)
        i = i + 1

    # breakを使って途中でループを抜ける
    print("\nbreakを使った繰り返し:")
    count = 0
    while True:  # 無限ループ
        print(count)
        count += 1  # count = count + 1 の省略形
        if count >= 5:
            break  # countが5以上になったらループを抜ける

    # continueを使って次のループへスキップ
    print("\ncontinueを使った繰り返し (偶数のみ表示):")
    i = 0
    while i < 10:
        i += 1
        if i % 2 == 1:  # iが奇数の場合
            continue  # 以降の処理をスキップして次のループへ
        print(i)

if __name__ == "__main__":
    main()
