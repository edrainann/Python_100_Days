#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10
# @Author  : Edrain


def is_palindrome(num):
    """"判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


def is_prime_01(num):
    """判断一个数是不是素数"""
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False


if __name__ == '__main__':
    num = int(input("请输入正整数："))
    if is_palindrome(num) and is_prime_01(num):
        print("{}是回文素数".format(num))
