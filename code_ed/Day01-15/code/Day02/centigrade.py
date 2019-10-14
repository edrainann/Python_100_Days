#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30
# @Author  : Edrain
"""
将华氏温度转换为摄氏温度

"""

# f = 100
# c = (f - 32)/1.8
# print(c)
#
# f = float(input("华氏温度= "))
# c = (f - 32) / 1.8
# print(c)

f = float(input("华氏温度= "))
c = (f - 32) / 1.8100
print('{}华氏度 = {}摄氏度'.format(f, c))
print('{}华氏度 = {:.2f}摄氏度'.format(f, c))
print('%.2f华氏度 = %.2f摄氏度' % (f, c))


