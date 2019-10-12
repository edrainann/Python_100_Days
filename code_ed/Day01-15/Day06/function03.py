#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8
# @Author  : Edrain


def add(*args):  # 在参数名前面的*表示args是一个可变参数
    total = 0
    for val in args:
        total += val
    return total


print(add())  # 在调用add函数时可以传入0个或多个参数
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 2, 3, 5, 7, 9))
