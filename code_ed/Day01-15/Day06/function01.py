#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8
# @Author  : Edrain


def factorial(num):
    """求阶乘"""
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


m = int(input("m = "))
n = int(input("n = "))
print(factorial(m) // factorial(n) // factorial(m - n))  # 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数
