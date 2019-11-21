#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21
# @Author  : Edrain


class TestDemo(object):
    def test_demo01(self):
        num = 12
        if num + 1 == 13:
            num = 23
            print("this is num_1: ", num)
        if num > 0:
            print("this is num_2:", num)  # 这个num = 23 了
