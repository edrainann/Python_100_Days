#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14
# @Author  : Edrain
import os
import sys

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

print(os.path.abspath('../../..'))

print('***获取ABSPATH***')
# ABSPATH = None
ABSPATH = os.path.abspath(sys.argv[0])
print(ABSPATH)
# 绝对路径
path1 = os.path.abspath('.')
# 相对路径
path2 = os.path.dirname('file_path.py')
path3 = os.path.dirname(path2)
print('-----', path3)

print('***获取test1***')
print(os.path.dirname(__file__))
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.dirname(os.path.abspath(__file__)))
print('--获取当前目录--', os.path.abspath("."))  # 获取当前目录
