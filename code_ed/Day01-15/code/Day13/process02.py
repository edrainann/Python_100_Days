#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22
# @Author  : Edrain
"""
使用多进程的方式将两个下载任务放到不同的进程中
通过Process类创建了进程对象，通过target参数我们传入一个函数来表示进程启动后要执行的代码，
后面的args是一个元组，它代表了传递给函数的参数。
Process对象的start方法用来启动进程，而join方法表示等待进程执行结束。
运行上面的代码可以明显发现两个下载任务“同时”启动了，而且程序的执行时间将大大缩短，不再是两个任务的时间总和。
"""
from multiprocessing import Process
from os import getpid
from random import randint
from time import sleep, time


def download_task(filename):
    print(f'启动下载进程器，进程号[{getpid():d}]')
    print(f'开始下载{filename}...')
    time_to_download = randint(1, 5)
    sleep(time_to_download)
    print(f'{filename}下载完成！耗费了{time_to_download}秒')


def main():
    start = time()
    p1 = Process(target=download_task, args=('--------Python从入门到脱发.pdf---------',))
    p1.start()  # Process对象的start方法用来启动进程
    p2 = Process(target=download_task, args=('========Good Study.avi==============',))
    p2.start()
    p1.join()  # join方法表示等待进程执行结束
    p2.join()
    end = time()
    print(f'总共花费了{end - start:.2f}')


if __name__ == '__main__':
    main()
