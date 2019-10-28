#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28
# @Author  : Edrain


class Women:
    def __init__(self, name):
        self.name = name
        self.age = 18

    def secret(self):
        print(f'{self.name} 的年龄是{self.age} ')


xf = Women("小芳")
print(xf.name)
print(xf.age)
xf.secret()
