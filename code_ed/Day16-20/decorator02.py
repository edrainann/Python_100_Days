#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24
# @Author  : Edrain
import logging


def use_logging(func):
    def wrapper():
        logging.warning(f'{func.__name__} is running')
        return func()

    return wrapper


@use_logging
def foo():
    print('i am foo')


foo()
