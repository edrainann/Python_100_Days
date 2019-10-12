#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11
# @Author  : Edrain
"""
如果一个函数包含 yield 表达式，那么它是一个生成器函数；调用它会返回一个特殊的迭代器，称为生成器。
生成器 gen 看起来和普通的函数没有太大区别。
仅只是将 return 换成了 yield。用 type() 函数打印二者的类型也能发现，func 和 gen 都是函数。
然而，二者的返回值的类型就不同了。func() 是一个 int 类型的对象；而 gen() 则是一个迭代器对象。
"""


def func():
    return 1


def gen():
    yield 1


print(type(func))
print(type(gen))

print(type(func()))
print(type(gen()))
