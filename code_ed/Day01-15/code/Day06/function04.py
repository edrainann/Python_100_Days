#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8
# @Author  : Edrain
"""
由于Python没有函数重载的概念，那么后面的定义会覆盖之前的定义，也就意味着两个函数同名函数实际上只有一个是存在的
"""


def foo():
    print("hello, world!")


def foo():
    print("goodbye, world!")


foo()