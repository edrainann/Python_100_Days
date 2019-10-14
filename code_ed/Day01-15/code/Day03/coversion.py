#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30
# @Author  : Edrain
"""
英制单位英寸和公制单位厘米互换
"""
# v1
# is_inch = int(input("请输入是否为请英制单位英寸，0为不是，1为是："))
# if is_inch == 1:
#     inch = float(input("请输入英制单位英寸："))
#     centimeter = inch / 0.03937
#     print(centimeter)
# elif is_inch == 0:
#     centimeter = float(input("请输入公制单位厘米："))
#     inch = centimeter * 0.03937
#     print(inch)
# else:
#     print("请重新输入数字0或者数字1")

# v2
# while True:
#     is_inch = int(input("请输入是否为请英制单位英寸，0为不是，1为是："))
#     if is_inch == 0 or is_inch == 1:
#         if is_inch == 1:
#             inch = float(input("请输入英制单位英寸："))
#             centimeter = inch / 0.03937
#             print(centimeter)
#         else:
#             centimeter = float(input("请输入公制单位厘米："))
#             inch = centimeter * 0.03937
#             print(inch)
#         break
#     else:
#         print("请重新输入数字0或者数字1")

# v3
value = float(input("请输入长度："))
unit = input("请输入单位：")
if unit == 'in' or unit == "英寸":
    print("{}英寸={}厘米".format(value, value * 2.54))
elif unit == "cm" or unit == "厘米":
    print("{}厘米={}英寸".format(value, value / 2.54))
else:
    print("请输入有效的单位")
