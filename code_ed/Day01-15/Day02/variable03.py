#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/29
# @Author  : Edrain

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))  # 乘
print('%d / %d = %f' % (a, b, a / b))  # 除
print('%d // %d = %d' % (a, b, a // b))  # 整除
print('%d %% %d = %d' % (a, b, a % b))  # 模，简单的理解就是取余数---20除以3, 商为6, 余数为2, 所以结果是2
print('%d ** %d = %d' % (a, b, a ** b))

