#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8
# @Author  : Edrain
"""
用for循环实现1~100求和
"""
sum = 0
for x in range(101):  # 可以产生一个0到100的整数序列。
    sum += x
print(sum)
