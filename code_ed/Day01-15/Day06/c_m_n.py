#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8
# @Author  : Edrain
"""
输入M和N计算C(M,N)
"""
m = int(input("请输入m="))
n = int(input("请输入n="))
fm = 1
for i in range(1, m + 1):
    fm *= m
fn = 1
for i in range(1, n + 1):
    fn *= m
fmn = 1
for i in range(1, m - n + 1):
    fmn *= i
print(fm // fn // fmn)
