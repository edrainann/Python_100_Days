#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11
# @Author  : Edrain
"""
通过__str__( )函数可以打印对象的属性信息:该对象此时的颜色为：~~~~~~~~~~~~五彩斑斓的黑~~~~~~~~~
如果没有__str__( )函数，执行print(cat)得到的结果为:<__main__.Cat object at 0x000001F42B33EDD8>
"""


class Cat:

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "该对象此时的颜色为：" + self.color

    def print_info(self):
        print()
        print("啦啦啦啦====这是print_info()打印出来的内容鸭")
        print(self.color)
        print()

    def eat(self):
        print("---------吃肉肉---------")


def main():
    # cat = Cat('~~~~~~~~~~~~五彩斑斓的黑~~~~~~~~~')
    # print(cat)
    # cat.print_info()
    # cat.eat()
    print(Cat)  # <class '__main__.Cat'>
    print(Cat("白白白"))  # 该对象此时的颜色为：白白白


if __name__ == '__main__':
    main()
