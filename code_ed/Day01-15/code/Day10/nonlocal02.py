#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14
# @Author  : Edrain
"""
nolocal 的使用场景就比较单一，它是使用在闭包中的，使变量使用外层的同名变量
"""


def foo(func):
    a = 1
    print("外层函数a的值", a)

    def wrapper():
        func()
        nonlocal a
        a = 0
        a += 1
        print("经过改变后，里外层函数a的值：", a)

    return wrapper


@foo
def change():
    print("nolocal的使用")


change()
