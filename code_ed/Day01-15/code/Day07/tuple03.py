#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25
# @Author  : Edrain


def sum_numbers(*args):
    num = 0
    print(args)
    # 循环遍历
    for n in args:
        # num = num + n
        num += n
    return num


result = sum_numbers((8, 2, 3, 4, 5))
print(result)


def sum_numbers02(args):
    num = 0
    print(args)
    # 循环遍历
    for n in args:
        # num = num + n
        num += n
    return num


result = sum_numbers02((8, 2, 3, 4, 5))  # TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
print(result)
