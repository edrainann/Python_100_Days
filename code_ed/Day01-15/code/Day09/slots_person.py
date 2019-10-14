#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12
# @Author  : Edrain
"""
__slots__魔法
Python是一门动态语言。
通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法，当然也可以对已经绑定的属性和方法进行解绑定。
但是如果我们需要限定自定义类型的对象只能绑定某些属性，可以通过在类中定义__slots__变量来进行限定。
需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用
"""


class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print(f'{self._name} 正在完飞行棋...')
        else:
            print(f'{self._name} 正在打麻将哈哈哈...')
            # print(f'{self._name} 正在打麻将哈哈哈...{self._gender}')  # AttributeError: _gender

    def __str__(self):
        return f'{self._name}、{self._age}、{self._gender}'


def main():
    person = Person('ed', 88)
    person.play()
    # print(person)  # AttributeError: _gender
    person._gender = '咦'
    print(person)  # ed、88、咦
    # person._is_what = "俺也不知道"  # 'Person' object has no attribute '_is_what'.


if __name__ == '__main__':
    main()
