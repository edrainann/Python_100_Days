#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25
# @Author  : Edrain
"""
不可变类型：
    数字类型-- int|bool|float|complex|long(2.x)
    字符串-- str
    元组-- tuple
可变类型：
    列表-- list
    字典-- dict
"""


def demo01(num, num_list):
    """可变类型、不可变类型

    :param num:不可变类型 内存中的数据不允许被修改
    :param num_list: 可变类型 内存中的数据可以被修改
    """
    print("内部函数")

    # 赋值语句
    num = 200
    # num_list = [1, 2, 3]

    # 可变类型可以方法调用来改变
    num_list.clear()
    num_list.extend([0, 8, 7])

    print(f'这是num的地址：{id(num)}，这是num的值：{num}')
    print(f'这是num_list的地址：{id(num_list)}，这是num_list的值：{num_list}')

    print("函数代码完成")
    print('-' * 100)


gl_num = 99
gl_list = [4, 5, 6]
demo01(gl_num, gl_list)
print(f'这是gl_num的地址:{id(gl_num)}，这是gl_num的值：{gl_num}')
print(f'这是gl_list的地址:{id(gl_list)}，这是gl_list的值：{gl_list}')
