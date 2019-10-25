#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25
# @Author  : Edrain
"""
多值参数的函数：
*args —— 存放 元组 参数，前面有一个 *
**kwargs —— 存放 字典 参数，前面有两个 **
"""


def sum_numbers(*args):
    num = 0

    print(f'这是函数内部的args：', args)

    return num, args


result = sum_numbers(1, 2, 3)
print('这是return出来的结', result)
print('-' * 50)
r_num, r_args = sum_numbers(7, 0, 9, 8)
print(f'this is t_num:{r_num}')
print(f'this is r_args:{r_args}')
