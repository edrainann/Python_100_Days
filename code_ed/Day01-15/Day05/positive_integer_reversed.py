#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8
# @Author  : Edrain
"""
正整数的反转
%    取模 - 返回除法的余数
//   取整除 - 返回商的整数部分（向下取整）
"""
number = int(input("请输入一个正整数："))
reversed_number = 0
while number > 0:
    reversed_number = reversed_number * 10 + number % 10
    number //= 10
print(reversed_number)
