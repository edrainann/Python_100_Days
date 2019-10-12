#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8
# @Author  : Edrain
"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3
"""
for number in range(100, 1000):
    low = number % 10  # 通过整除和求模运算分别找出了一个三位数的个位、十位和百位
    mid = number // 10 % 10
    high = number // 100
    if number == low ** 3 + mid ** 3 + high ** 3:
        print(number)
