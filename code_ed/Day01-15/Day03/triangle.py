#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30
# @Author  : Edrain
import math
"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积
"""
a = float(input("请输入三角形的边长："))
b = float(input("请输入三角形的边长："))
c = float(input("请输入三角形的边长："))
if a + b > c or a + c > b:
    perimeter = a + b + c
    p = perimeter / 2
    # area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    # area = math.sqrt(p * (p-a)*(p-b)*(p-c))  #  开根号，三角形的三边面积计算--海伦公式
    a = p * (p-a)*(p-b)*(p-c)
    area = pow(a, 1/2)  # x的y次方
    print("三角形的周长是：{}".format(perimeter))
    print("三角形的面积是：{}".format(area))
else:
    print("输入的这三条边不能构成三角形。")
