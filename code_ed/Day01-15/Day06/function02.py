#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8
# @Author  : Edrain
from random import randint


def roll_dice(n=2):
    """摇色子"""
    total = 0
    for i in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c


print(roll_dice())  # 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice(3))  # 摇三颗色子
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(c=44, a=100, b=3))  # 传递参数时可以不按照设定的顺序进行传递
