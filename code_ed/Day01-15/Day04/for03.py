#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8
# @Author  : Edrain
"""
用for循环实现1~100之间的偶数求和
"""
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
print(sum)
