#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14
# @Author  : Edrain
"""
global很明显就是声明代码块中的变量使用外部全局的同名变量
"""
a = 1


def change():
    global a
    a += 1
    print("函数内部的a的值：", a)  # 2


change()
print("调用change函数后， 函数外部的a的值：", a)  # 2
