"""
面积计算器 —— 我的第一个 Python 项目

支持计算圆、矩形、三角形的面积。
运行：python area.py
"""

import math


def read_positive(prompt):
    """反复要求输入，直到拿到一个正数为止。"""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("  [!] 请输入数字")
            continue
        if value > 0:
            return value
        print("  [!] 请输入正数")


def circle_area(r):
    """圆的面积：S = πr²"""
    return math.pi * r * r


def rectangle_area(a, b):
    """矩形的面积：S = ab"""
    return a * b


def triangle_area(base, height):
    """三角形的面积：S = 底 × 高 ÷ 2"""
    return 0.5 * base * height


def main():
    while True:
        print()
        print("======== 面积计算器 ========")
        print("  1. 圆")
        print("  2. 矩形 / 正方形")
        print("  3. 三角形")
        print("  0. 退出")
        print("============================")

        choice = input("请选择 (0-3): ").strip()

        if choice == "0":
            print("再见！")
            break

        elif choice == "1":
            r = read_positive("请输入半径 r: ")
            print(f"\n  圆的面积 = {circle_area(r):.6f}\n")

        elif choice == "2":
            a = read_positive("请输入长 a: ")
            b = read_positive("请输入宽 b: ")
            print(f"\n  矩形的面积 = {rectangle_area(a, b):.6f}\n")

        elif choice == "3":
            base = read_positive("请输入底: ")
            height = read_positive("请输入高: ")
            print(f"\n  三角形的面积 = {triangle_area(base, height):.6f}\n")

        else:
            print("\n  [!] 没有这个选项，请输入 0-3\n")


if __name__ == "__main__":
    main()
