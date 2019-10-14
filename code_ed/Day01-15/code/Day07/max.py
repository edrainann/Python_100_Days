#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11
# @Author  : Edrain


def max2(x):
    """
    设计一个函数返回传入的列表中最大和第二大的元素的值。
    :param x: 是一个列表 list[]
    :return: 排序，找出列表中 最大 和 第二大 的两个值
    """
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


x = [1, 6777, 3, 2, 44, 55, 11, 98, 2, 1111]
print(max2(x))

