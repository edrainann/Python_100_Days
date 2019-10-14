#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11
# @Author  : Edrain
"""
设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
"""
import random


def generate_code_01(n):
    code = 0
    a = random.randint(0, 9)
    for _ in range(n):
        code += a
        # print(a)
        # print(code)
    return code


def generate_code_02(code_len=4):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


if __name__ == '__main__':
    print(generate_code_01(2))
    print(generate_code_02())
