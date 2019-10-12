#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8
# @Author  : Edrain
"""
输出乘法口诀表(九九表)
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        multiply = i * j
        print("{}*{}={}".format(i, j, multiply), end='\t')
    print()
