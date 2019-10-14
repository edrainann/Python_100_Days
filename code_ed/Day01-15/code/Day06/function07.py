#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10
# @Author  : Edrain
""""
使用global关键字来指示foo函数中的变量a来自于全局作用域。
如果全局作用域中没有a，那么下面一行的代码就会定义变量a并将其置于全局作用域。
事实上，减少对全局变量的使用，也是降低代码之间耦合度的一个重要举措，同时也是对迪米特法则的践行。
"""


def foo():
    global a
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 200
