#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8
# @Author  : Edrain
"""
输入两个正整数计算它们的最大公约数和最小公倍数
"""
a = int(input("请输入第一个正整数："))
b = int(input("请输入第二个正整数："))
if a > b:
    a, b = b, a
for factor in range(a, 0, -1):
    if a % factor == 0 and b % factor == 0:
        print("{}和{}的最大公约数是{}".format(a, b, factor))
        print("{}和{}的最小公倍数是{}".format(a, b, a * b // factor))
        break
