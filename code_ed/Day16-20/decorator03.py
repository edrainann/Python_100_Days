# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 
# @Author  : Edrain
import time


def display_time(func):
    """装饰器--传入不带参数"""

    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print(t2 - t1)

    return wrapper


def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def prime_num():
    t1 = time.time()
    for i in range(2, 2000):
        if is_prime(i):
            print(i)
    t2 = time.time()
    print(t2 - t1)


@display_time
def prime_num_dec():
    for i in range(2, 2000):
        if is_prime(i):
            print(i)


def display_time_result(func):
    """装饰器--返回运行结果"""

    def wrapper():
        t1 = time.time()
        result = func()
        t2 = time.time()
        print(f'Total time:{t2 - t1:.4f}')
        return result

    return wrapper


@display_time_result
def count_prime_nums_result():
    count = 0
    for i in range(2, 2000):
        if is_prime(i):
            count = count + 1
    return count


def display_time_param(func):
    """装饰器--传入参数"""

    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print(t2 - t1)
        return result

    return wrapper


@display_time_param
def count_prime_nums_param(max_num):
    count = 0
    for i in range(2, max_num):
        if is_prime(i):
            count = count + 1
    return count


prime_num()
print('-' * 50)
prime_num_dec()
print('-' * 50)
print(count_prime_nums_result())
print('-' * 50)
# count = count_prime_nums_param()
print(count_prime_nums_param(2000))
