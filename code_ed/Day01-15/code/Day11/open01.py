#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14
# @Author  : Edrain
import os
from time import sleep


def main01():
    f = open('清晨一定会来.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()


def main02():
    f = None
    try:
        f = open('清晨一定会来.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误！！')
    finally:
        if f:
            print('执行---f.close')
            f.close()
            print('执行===f.close')


def main03():
    path = os.path.abspath(os.path.join(os.getcwd(), "../../res"))
    # path1 = os.path.abspath(os.path.join(os.getcwd(), "../../res/清晨一定会来.txt"))
    try:
        # with open(path1, 'r', encoding='utf-8') as f:
        with open(path + '\\清晨一定会来.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误！！')


def main04():
    # 一次性读取整个文件内容
    path = os.path.abspath(os.path.join(os.getcwd(), "../../res"))
    with open(path + '\\清晨一定会来.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    # UnicodeDecodeError: 'gbk' codec can't decode byte 0xab in position 27: illegal multibyte sequence
    # with open(path + '\\清晨一定会来.txt', mode='rb') as f: 或者encoding='utf-8'解决
    with open(path + '\\清晨一定会来.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    # UnicodeDecodeError: 'gbk' codec can't decode byte 0xab in position 27: illegal multibyte sequence
    with open(path + '\\清晨一定会来.txt') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main04()
