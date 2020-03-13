# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 
# @Author  : Edrain


def is_num(x):
    """判断str是否为纯数字"""
    try:
        int_x = int(x)
        return int_x
    except:
        print("有非纯数字")


if __name__ == '__main__':
    a = "123"
    print(is_num(a))
