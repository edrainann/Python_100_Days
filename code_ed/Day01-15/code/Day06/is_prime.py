#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/9
# @Author  : Edrain


def is_prime_01(num):
    """判断一个数是不是素数"""
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False


num = 3
print(is_prime_01(num))


def is_prime_02(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    tag = False
    if num != 1:
        tag = True
    return tag


print(is_prime_02(num))
