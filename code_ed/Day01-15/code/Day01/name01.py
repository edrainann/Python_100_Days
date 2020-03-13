# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 
# @Author  : Edrain
import operator


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'name=%s, age=%s' % (self.name, self.age)


xmr = Person('ed', 12)
print(xmr.name)
print(xmr.__dict__['name'])  # 通过属性字典__dict__
print(getattr(xmr, 'name'))  # 通过getattr函数
print(operator.attrgetter('name'))
