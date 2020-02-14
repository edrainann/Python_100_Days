#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6
# @Author  : Edrain
from functools import wraps


def demo_test(func):
    @wraps(func)
    def inner_func():
        inner_obj = 'inner_obj'
        print(inner_obj)
        return func(inner_obj)  #

    return inner_func


@demo_test
def demo_test_func(obj):
    print('---', obj)  #
    # return False
    return obj


a = demo_test_func()
print(a)
b = a + "abc"
print(b)
