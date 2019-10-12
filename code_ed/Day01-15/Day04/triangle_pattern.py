#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8
# @Author  : Edrain
"""
打印三角形图案
"""

row = int(input("请输入行数："))
for i in range(row):  # 可以产生一个0到row-1的整数序列。
    for j in range(i + 1):
        print("*", end='')
    print()
print()

for a in range(row):
    for b in range(row):
        if b < row - a - 1:
            print("_", end="")
        else:
            print("*", end="")
    print()
print()

for x in range(row):
    for y in range(row - x - 1):
        print("_", end="")
    for y in range(2 * x + 1):
        print("*", end="")
    print()
