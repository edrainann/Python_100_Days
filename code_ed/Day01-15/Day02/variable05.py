#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30
# @Author  : Edrain
"""
比较、逻辑和算身份运算符的使用
"""
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not(1 != 2)
print('flag0=', flag0)  # true
print('flag1=', flag1)  # True
print('flag2=', flag2)  # False
print('flag3=', flag3)  # False, and是逻辑判断，返回的是真（非0值）或者假（值0），在算式a and b中，只要a、b中有一个为0就返回0（假）值。否则就返回b的值。
print('flag4=', flag4)  # True
print('flag5=', flag5)
print(flag1 is True)
print(flag1 is not True)


