#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8
# @Author  : Edrain
"""
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只
"""
for cock in range(20):
    for hen in range(33):
        chick = 100 - cock - hen
        if 5 * cock + 3 * hen + chick / 3 == 100:
            print("公鸡：{}只，母鸡：{}只，小鸡：{}只".format(cock, hen, chick))
