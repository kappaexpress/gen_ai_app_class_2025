#!/usr/bin/env python3
# ライブラリのインポートのサンプル

import statistics  # 統計計算のライブラリ
import math        # 数学関数のライブラリ


def main():
    # statisticsライブラリを使った統計計算
    print("statisticsライブラリを使った統計計算:")
    linumber = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"平均: {statistics.mean(linumber)}")
    print(f"標準偏差: {statistics.stdev(linumber)}")
    print(f"中央値: {statistics.median(linumber)}")

    # mathライブラリを使った数学計算
    print("\nmathライブラリを使った数学計算:")
    x = 10
    print(f"log_10({x}): {math.log10(x)}")
    print(f"log_2({x}): {math.log2(x)}")
    print(f"log_e({x}): {math.log(x)}")
    print(f"sqrt({x}): {math.sqrt(x)}")

    # 三角関数の計算
    print("\n三角関数の計算:")
    angle_degrees = 180
    angle_radians = math.radians(angle_degrees)  # 度をラジアンに変換
    print(f"{angle_degrees}度 = {angle_radians}ラジアン")
    print(f"sin({angle_degrees}度): {math.sin(angle_radians)}")
    print(f"cos({angle_degrees}度): {math.cos(angle_radians)}")
    print(f"tan({angle_degrees}度): {math.tan(angle_radians)}")

    # 円周率と自然対数の底
    print("\n数学定数:")
    print(f"円周率 π: {math.pi}")
    print(f"自然対数の底 e: {math.e}")

    # その他の便利な関数
    print("\nその他の便利な関数:")
    print(f"切り上げ ceil(3.2): {math.ceil(3.2)}")
    print(f"切り捨て floor(3.8): {math.floor(3.8)}")
    print(f"絶対値 fabs(-5.5): {math.fabs(-5.5)}")
    print(f"べき乗 pow(2, 3): {math.pow(2, 3)}")


if __name__ == "__main__":
    main()
