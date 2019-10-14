#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11
# @Author  : Edrain
"""
在屏幕上显示跑马灯文字。
"""
import os
import time


def main():
    content = '有没有那么一首歌， '
    while True:
        # # 清理屏幕上的输出
        os.system('cls')  # for Windows use os.system('cls') instead
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]
        print("======", content[0])


if __name__ == '__main__':
    main()
