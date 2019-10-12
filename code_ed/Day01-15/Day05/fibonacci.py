#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8
# @Author  : Edrain
"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...
"""
a = 0
b = 1
for i in range(20):
    # a, b = b, a + b
    # 关于 a, b = b, a + b 的解读v1
    # tmp = a
    # a = b
    # b = tmp + b
    # 关于 a, b = b, a + b 的解读v2
    c = a + b
    a = b
    b = c
    print(a, end=" ")
