#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10
# @Author  : Edrain
"""所谓字符串，就是由零个或多个字符组成的有限序列
在Python程序中，如果我们把单个或多个字符用单引号或者双引号包围起来，就可以表示一个字符串。
"""

s1 = 'hello, world!'
s2 = "hello,world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello,
world!
还以为放在这个里面的都是注释诶，木有想到还可以这么玩。。。
"""
print(s1, s2, s3, end="")
