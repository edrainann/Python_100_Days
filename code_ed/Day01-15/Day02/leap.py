#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30
# @Author  : Edrain
"""
输入年份 如果是闰年输出True 否则输出False
"""
# V1
# year = int(input("请输入年份="))
# # year = 2006
# # print(type(year/4))
# # print(year/4)
# # print(year//4)
# # print(year % 4)
# if year % 4 == 0:
#     print(True)
# else:
#     print(False)

year = int(input("请输入年份="))
is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(is_leap)


