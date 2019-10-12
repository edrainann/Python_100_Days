#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10
# @Author  : Edrain
"""
如果不希望字符串中的\表示转义，我们可以通过在字符串的最前面加上字母r来加以说明
"""

s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')
