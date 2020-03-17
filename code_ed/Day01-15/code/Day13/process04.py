# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 
# @Author  : Edrain
from multiprocessing import Process
import os


def run_child_process(name):
    # pid：process id子进程， ppid：parent's process id父进程
    print(f'开始运行子进程的名字:{name}，子进程的进程号:{os.getpid()}')


if __name__ == "__main__":
    print(f'父进程的进程号:{os.getpid()}')
    # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例
    p = Process(target=run_child_process, args=('ed',))
    print('子进程将会 开始...')
    # 用start()方法启动
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    p.join()
    print('子进程将会 结束...')
