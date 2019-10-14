#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14
# @Author  : Edrain
import os

print("---获取当前目录-----")
print(os.getcwd())
print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.abspath('.'))
print(os.path.abspath(os.path.join(os.getcwd(), ".")))
print()

print('***获取上级目录***')
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print(os.path.abspath(os.path.dirname(os.getcwd())))
print(os.path.abspath(os.path.join(os.getcwd(), "..")))
print()

print('***获取上上级目录***')
print(os.path.abspath(os.path.join(os.getcwd(), "../..")))
print(os.path.abspath(os.path.join(os.getcwd(), "../res")))

print()
