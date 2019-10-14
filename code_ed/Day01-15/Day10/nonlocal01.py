#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14
# @Author  : Edrain
i = 0


def a():
    i = 1

    def b():
        nonlocal i  # 修改Enclosing变量的问题，就需要使用nonlocal关键字
        i = 2

    b()
    print(i)  # 2


a()
