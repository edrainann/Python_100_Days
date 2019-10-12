#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12
# @Author  : Edrain
"""
@property装饰器
之前我们讨论过Python中属性和方法访问权限的问题，
虽然我们不建议将属性设置为私有的，但是如果直接将属性暴露给外界也是有问题的，比如我们没有办法检查赋给属性的值是否有效。
我们之前的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，不建议外界直接访问，
那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作。
如果要做到这点，就可以考虑使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便，
"""


class Person(object):

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
            print(f'{self._name} 正在完飞行棋')
        else:
            print(f'{self._name} 正在打麻将哈哈哈')


def main():
    person = Person('ed', 88)
    person.play()
    person.age = 8
    person.play()


if __name__ == '__main__':
    main()
