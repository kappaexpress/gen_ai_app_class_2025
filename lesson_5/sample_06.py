#!/usr/bin/env python3
# 条件分岐 (if) のサンプル

def main():
    # 基本的なif文
    print("基本的なif文:")
    for i in range(5):
        if i == 2:
            print(f"{i}は2です")

    # if-else文
    print("\nif-else文:")
    for i in range(5):
        if i == 2:
            print(f"{i}は2です")
        else:
            print(f"{i}は2ではありません")

    # if-elif-else文
    print("\nif-elif-else文:")
    dict_a = {"January": "1", "February": "2", "May": "5"}
    for k in dict_a.keys():
        if k == "January":
            print(dict_a[k])
        elif dict_a[k] == "2":
            print(f"{k} corresponds to {dict_a[k]} in dict_a.")
        else:
            print(f"{k} is not January or February.")

    # 比較演算子の例
    print("\n比較演算子の例:")
    x = 10
    if x > 5:
        print(f"{x}は5より大きい")
    if x >= 10:
        print(f"{x}は10以上")
    if x < 20:
        print(f"{x}は20より小さい")
    if x <= 10:
        print(f"{x}は10以下")
    if x != 5:
        print(f"{x}は5と等しくない")

    # 論理演算子 (and, or, not) の例
    print("\n論理演算子の例:")
    age = 25
    if age >= 18 and age < 65:
        print("成人で65歳未満です")

    weather = "rainy"
    if weather == "sunny" or weather == "cloudy":
        print("傘は不要です")
    else:
        print("傘が必要です")

if __name__ == "__main__":
    main()
