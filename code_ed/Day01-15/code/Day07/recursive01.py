# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 
# @Author  : Edrain
"""
递归
"""


def sum_number(num):
    print(num)
    # 递归的出口，当参数满足某个条件时，不再执行函数
    if num == 1:
        return
    sum_number(num - 1)
    print(f'this is {num}', '-' * 8)


print("it is over:",sum_number(3))
