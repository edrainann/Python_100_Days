#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22
# @Author  : Edrain
"""
替换字符串中的不良内容
 re模块的正则表达式相关函数中都有一个flags参数，它代表了正则表达式的匹配标记，
 可以通过该标记来指定匹配时是否忽略大小写、是否进行多行匹配、是否显示调试信息等。
 如果需要为flags参数指定多个值，可以使用按位或运算符进行叠加，如flags=re.I | re.M。
"""
import re


def main():
    sentence = '哎鸭鸭，这些里面鸭有不良的内容鸭...啧啧啧不良'
    purified = re.sub('[不良]|鸭',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)  # 哎**，这些里面*有**的内容*...啧啧啧**


if __name__ == '__main__':
    main()
