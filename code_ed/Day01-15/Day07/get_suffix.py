#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11
# @Author  : Edrain


def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名
    :param filename:文件名
    :param has_dot:返回的后缀名是否需要带点
    :return:文件的后缀名
    rfind() 返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1
    三元表达式
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


print(get_suffix('document.txt'))
