# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 
# @Author  : Edrain
from multiprocessing import Pool
import os
import time
import random

"""
如果要启动大量的子进程，可以用进程池的方式批量创建子进程
"""


def long_time_task(name):
    print(f'启动任务名字：{name}，任务进程号：{os.getpid()}')
    start = time.time()
    time.sleep(random.random() * 3)  #  random.random()产生 0 到 1 之间的随机浮点数
    end = time.time()
    need_time = end - start
    print(f'任务名字：{name}，花费时间：{need_time:.2f}')


if __name__ == '__main__':
    """
    代码解读：
    对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。
    这是Pool有意设计的限制，并不是操作系统的限制。如果改成：p = Pool(5)
    """
    print(f'父进程的进程号:{os.getpid()}')
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('等待所有子进程结束...')
    p.close()
    p.join()
    print('所有子进程结束')

