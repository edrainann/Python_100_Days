#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10
# @Author  : Edrain
"""
在字符串中使用 \反斜杠 来表示转义，也就是说 \ 后面的字符不再是它原来的意义，
例如：\n不是代表反斜杠和字符n，而是表示换行；
而\t也不是代表反斜杠和字符t，而是表示制表符。
所以如果想在字符串中表示'要写成\'，同理想表示\要写成\\。
"""

s1 = '\'hello world!\''
s2 = '\n\\hello world!\\\n'
print("-----")
print(s1, s2, end="")
print("++++++")
