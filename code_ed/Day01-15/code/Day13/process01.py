#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22
# @Author  : Edrain
"""
用一个下载文件的例子来说明使用多进程和不使用多进程到底有什么差别
这个例子可以看出，如果程序中的代码只能按顺序一点点的往下执行，
那么即使执行两个毫不相关的下载任务，也需要先等待一个文件下载完成后才能开始下一个下载任务，很显然这并不合理也没有效率。
"""
from random import randint
from time import sleep, time


def download_task(filename):
    print(f'开始下载{filename}')
    time_to_download = randint(1, 5)
    sleep(time_to_download)
    print(f'{filename}下载完成！耗费了{time_to_download}秒')


def main():
    start = time()
    download_task('--------Python从入门到脱发.pdf--------------')
    download_task('========Good Study.avi==============')
    end = time()
    print(f'总共耗费了{end - start}')
    print(f'总共耗费了{end - start:.2f}')


if __name__ == '__main__':
    main()
