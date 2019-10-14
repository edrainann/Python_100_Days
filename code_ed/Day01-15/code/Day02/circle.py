#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30
# @Author  : Edrain
"""
输入半径计算圆的周长和面积
"""
# # V1
# r = float(input('圆的半径='))
# perimeter = 2 * 3.14 * r
# area = 3.14 * r * r
# print(perimeter)
# print(area)

import math

radius = float(input('圆的半径='))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print("周长为：{:.2f}".format(perimeter))
print("面积为：{:.2f}".format(area))
