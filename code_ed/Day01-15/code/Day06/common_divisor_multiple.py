#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8
# @Author  : Edrain


def gcd(x, y):
    """求最大公约数"""
    if x > y:
        # x, y = y, x
        tmp = x
        x = y
        y = tmp
        for factor in range(x, 0, -1):
            if x % factor == 0 and y % factor == 0:
                return factor


def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)


if __name__ == '__main__':
    print("最大公约数:", gcd(22, 3))
    print("最小公倍数", lcm(22, 3))
