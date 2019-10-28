#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28
# @Author  : Edrain
"""
python中的私有属性和私有方法
在外界访问python中的私有属性和私有方法
"""


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
xf.secret01()
# xf.__secret02()  # 私有方法，同样不允许在外界直接访问
xf._Women__secret02()  # Python 中，并没有 真正意义 的 私有
