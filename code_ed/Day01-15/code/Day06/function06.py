#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10
# @Author  : Edrain


def foo():
    a = 200
    print("foo:", a)  # foo: 200


if __name__ == '__main__':
    a = 100
    foo()
    print("---------")
    print("main:", a)  # main: 100
