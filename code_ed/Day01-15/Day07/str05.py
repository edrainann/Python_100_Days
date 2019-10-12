#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10
# @Author  : Edrain
"""
Python为字符串类型提供了非常丰富的运算符，
我们可以使用+运算符来实现字符串的拼接，
可以使用*运算符来重复一个字符串的内容，
可以使用in和not in来判断一个字符串是否包含另外一个字符串（成员运算），
我们也可以用[]和[:]运算符从字符串取出某个字符或某些字符（切片运算）
"""

s1 = 'hello ' * 3
print(s1)  # hello hello hello
s2 = 'world'
s1 += s2
print(s1)  # hello hello hello world
print("ll" in s1)  # True
print("edrain" in s1)  # False
str2 = 'abc123456'
print((str2[2]))  # c
print(str2[2:5])  # c12
print(str2[2:])  # c123456
print(str2[2::2])  # c246, 后面的数 每两个取一个
print(str2[::2])  # ac246, 前面的数 每两个取一个
print(str2[::-1])  # 654321cba， [-1]取倒数第一个元素
print(str2[-3])  # 4
print(str2[-3:])  # 456
print(str2[-1])  # 6
print(str2[:-1])  # abc12345
print(str2[-3:-1])  # 45
