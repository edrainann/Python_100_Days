#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24
# @Author  : Edrain
"""
简单装饰器
"""
import logging


def use_logging(func):
    def wrapper():
        logging.warning(f'{func.__name__} is running')
        return func()

    # print('type(wrapper):', type(wrapper))
    # print('type(wrapper()):', type(wrapper()))
    return wrapper


def foo():
    print('i am foo')


foo = use_logging(foo)
print('------------------')
foo()
