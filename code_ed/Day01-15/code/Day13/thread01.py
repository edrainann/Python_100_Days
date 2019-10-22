#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22
# @Author  : Edrain
"""
在Python早期的版本中就引入了thread模块（现在名为_thread）来实现多线程编程，然而该模块过于底层，而且很多功能都没有提供，
因此目前的多线程开发我们推荐使用threading模块，该模块对多线程编程提供了更好的面向对象的封装。
我们把刚才下载文件的例子用 多线程 的方式来实现一遍。
"""
from random import randint
from threading import Thread
from time import sleep, time


def download(filename):
    print(f'开始下载{filename}...')
    time_to_download = randint(1, 5)
    sleep(time_to_download)
    print(f'{filename}下载完成！耗费了{time_to_download}秒')


def main():
    start = time()
    t1 = Thread(target=download, args=('--------Python从入门到脱发.pdf---------',))
    t1.start()
    t2 = Thread(target=download, args=('========Good Study.avi==============',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print(f'总共耗费了{end - start:.3f}')


if __name__ == '__main__':
    main()
