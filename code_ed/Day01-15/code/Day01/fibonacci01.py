# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 
# @Author  : Edrain

"""
斐波那契序列的求值函数，参数为n，返回第n位的值，
默认第0位是1，第1位是1
"""


def feb(n):
    """递归函数
       输出斐波那契数列"""
    if n <= 1:
        return 1
    else:
        return feb(n - 1) + feb(n - 2)


def output_feb(n):
    feb_str = ""
    for i in range(n):
        feb_str = f'{feb_str}\n{feb(i)}'
    return feb_str


if __name__ == '__main__':
    x = 4
    # print(feb(x))
    print(output_feb(x))
