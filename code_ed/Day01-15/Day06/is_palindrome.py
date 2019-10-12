#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/9
# @Author  : Edrain


def is_palindrome(num):
    """"判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


num = 43
print(is_palindrome(num))
