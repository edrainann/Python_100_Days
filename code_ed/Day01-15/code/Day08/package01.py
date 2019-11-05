#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28
# @Author  : Edrain


class Person:

    def __init__(self, name, weight):
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'我的名字叫{self.name}，体重是{self.weight:.2f}公斤'
        # return "我的名字叫 %s 体重是%.2f" % (self.name, self.weight)

    def run(self):
        pass

    def eat(self):
        pass


xm = Person("小明", 86.6)
xm.run()
xm.eat()
print(xm)  # 使用print输出对象变量
