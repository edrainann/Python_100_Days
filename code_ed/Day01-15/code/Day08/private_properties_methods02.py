#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28
# @Author  : Edrain


class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def secret01(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print(f'{self.name} 的年龄是{self.__age} ')

    def __secret02(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print(f'{self.name} 的年龄是{self.__age} ')


xf = Women("小芳")
print(xf.name)
# 私有属性，在外界不能够直接访问
print(xf.__age)
xf.secret01()
# 私有方法，同样不允许在外界直接访问
xf.__secrest02()
