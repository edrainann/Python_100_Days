#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22
# @Author  : Edrain
"""
直接使用threading模块的Thread类来创建线程，但是我们之前讲过一个非常重要的概念叫“继承”，我们可以从已有的类创建新类，
因此也可以通过继承Thread类的方式来创建自定义的线程类，然后再创建线程对象并启动线程。
"""
from random import randint
from threading import Thread
from time import sleep, time


class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print(f'开始下载{self._filename}...')
        time_to_download = randint(1, 5)
        sleep(time_to_download)
        print(f'{self._filename}下载完成！耗费了{time_to_download}秒')


def main():
    start = time()
    t1 = DownloadTask('--------Python从入门到脱发.pdf---------')
    t1.start()
    t2 = DownloadTask('========Good Study.avi==============')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print(f'总共耗费了{end - start:.2f}')


if __name__ == '__main__':
    main()
