#!/usr/bin/env python3
# 変数のサンプル

def main():
    # 数値の変数
    a = 3  # assign a value "3" to a variable "a"
    b = 18
    print(a + b)  # addition
    print(a - b)  # subtraction
    print(b / a)  # division
    print(a * b)  # multiplication

    # 文字列の変数
    greeting = "Hello world"
    print(greeting)

    # 変数名として使える例
    aaa = 5
    my_value = 10
    value_123 = 15

    # 変数の中身を文字列の中で展開する（format()を使う）
    name = "Ken"
    age = 6
    print("{}, which is {} years old is now sitting.".format(name, age))

    # f-stringsを使った変数展開（Python 3.6以降）
    print(f"{name}, which is {age} years old is now sitting.")

if __name__ == "__main__":
    main()
