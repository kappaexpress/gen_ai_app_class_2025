#!/usr/bin/env python3
# 関数のサンプル

def main():
    # 関数の呼び出し (引数なし)
    print("関数の呼び出し (引数なし):")
    func_1()

    # 引数を持つ関数の呼び出し
    print("\n引数を持つ関数の呼び出し:")
    str_1 = "Python"
    func_2(str_1)

    # 戻り値を持つ関数の呼び出し
    print("\n戻り値を持つ関数の呼び出し:")
    numbers = [2, 4, 5, -2, 3]
    result_1 = summation(numbers)
    print(f"合計: {result_1}")

    # 複数の引数と戻り値を持つ関数
    print("\n複数の引数と戻り値を持つ関数:")
    result_2 = calculate(10, 5)
    print(f"加算: {result_2[0]}, 減算: {result_2[1]}")

    # デフォルト引数を持つ関数
    print("\nデフォルト引数を持つ関数:")
    greet()
    greet("太郎")


def func_1():
    """引数なし、戻り値なしの関数"""
    print("Hello")


def func_2(arg_1):
    """引数あり、戻り値なしの関数"""
    print(f"Hello {arg_1}")


def summation(arg_1):
    """リストの合計を計算する関数"""
    sumvalue = 0
    for number in arg_1:
        sumvalue = sumvalue + number
    return sumvalue  # 結果を返す


def calculate(a, b):
    """2つの数値の加算と減算を行う関数"""
    addition = a + b
    subtraction = a - b
    return addition, subtraction  # 複数の値を返す (タプルとして返される)


def greet(name="名無し"):
    """デフォルト引数を持つ関数"""
    print(f"こんにちは、{name}さん")


if __name__ == "__main__":
    main()
