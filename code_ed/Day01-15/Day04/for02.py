#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8
# @Author  : Edrain
"""
用for循环实现1~100之间的偶数求和
"""
sum = 0
for i in range(2, 101, 2):  # 左闭，右开。可以产生一个2到100的偶数序列，其中2是步长，即数值序列的增量
    sum += i
print(sum)
