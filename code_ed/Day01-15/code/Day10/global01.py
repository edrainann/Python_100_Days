#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14
# @Author  : Edrain
"""
global很明显就是声明代码块中的变量使用外部全局的同名变量
"""
a = 1


def change():
    # global a
    # a += 1
    a = 2
    print("函数内部的a的值：", a)  # 2


def change02():
    print("使用全局变量 a的值：", a)  # 2


change()
print("调用change函数后， 函数外部的a的值：", a)
change02()

num = 10
print('---', id(num))


def demo01():
    num = 1
    print('demo01 --》', num, id(num))


demo01()

a = 3


def demo02():
    global a  # 调用全局变量a
    print("demo02--", a)  # 1 ，demo02方法里之后再调用a时，都是全局的a
    a = a + 20


if __name__ == "__main__":
    """执行顺序2、1、3"""
    print(a)  # 2
    a = a + 10
    demo02()
    print("end--", a)  # 3 ,demo02 改变了最后a的输出值
