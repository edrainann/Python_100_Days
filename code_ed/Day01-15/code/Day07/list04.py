#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10
# @Author  : Edrain
"""
list 的 sorted 函数  -- 不会改变 list 本身顺序
list 的 sort 函数  -- 会改变 list 本身顺序
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
Q：key = len 抛 Expected type 'Optional[(str) -> Any]' (matched generic type 'Optional[(_T) -> Any]'), got '(o: Sized) -> int' instead
A：暂时不知道这样写有什么问题，程序是可以执行的。
"""
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
print(list1)  # ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
print(list2)  # ['apple', 'blueberry', 'internationalization', 'orange', 'zoo']

list3 = sorted(list1, reverse=True)  # ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)  # ['zoo', 'apple', 'orange', 'blueberry', 'internationalization'],
print("list3:", list3)
print("list4:", list4)

list1.sort()
# list1.sort(reverse=True)
print(list1)

name_list = ['allen', 'ann', 'ed', 'ann']
print('-======', name_list.index('ann'))
list_len = len(name_list)
print(list_len)
name_list.sort(reverse=True)  # 降序排列
