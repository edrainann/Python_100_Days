#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14
# @Author  : Edrain
"""
global很明显就是声明代码块中的变量使用外部全局的同名变量
"""
a = 1


def change():
    # global a
    # a += 1
    a = 2
    print("函数内部的a的值：", a)  # 2


def change02():
    print("使用全局变量 a的值：", a)  # 2


change()
print("调用change函数后， 函数外部的a的值：", a)
change02()

num = 10
print('---', id(num))


def demo01():
    num = 1
    print('demo01 --》', num, id(num))


demo01()
