#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8
# @Author  : Edrain
"""
输入一个正整数判断它是不是素数
"""
from math import sqrt

number = int(input("请输入一个正整数："))
end = int(sqrt(number))
is_prime = True
for x in range(2, end + 1):
    if number % x == 0:
        is_prime = False
        break
if is_prime and number != 1:
    print("{}是素数".format(number))
else:
    print("{}不是素数".format(number))
