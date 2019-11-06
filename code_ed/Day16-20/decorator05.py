# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 
# @Author  : Edrain
"""把类的构造函数当成了一个装饰器，它接受一个函数作为参数，并返回了一个对象，
而由于对象实现了 __call__ 方法，因此返回的对象相当于返回了一个函数。
因此该类的构造函数就是一个装饰器。
"""
from time import time


class Timer:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        before = time()
        result = self._func(*args, **kwargs)
        after = time()
        print("elapsed: ", after - before)
        return result


@Timer
def add(x, y=10):
    return x + y


a = add(4893849394)
print(a, "_abv")
