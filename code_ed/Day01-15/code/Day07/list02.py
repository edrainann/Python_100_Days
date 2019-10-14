#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10
# @Author  : Edrain
"""
预先定义了一个list
list1 = [1,2,3,4]      #这么用好
比
list1 = [1,2,3]        #这么用不好
list1.append(4)
此时会出现该提示
"""

list1 = [1, 3, 5, 7, 100]
# 添加元素
list1.insert(0, 400)  # [400, 1, 3, 5, 7, 100, 222, 1000, 2000]
list1.append(222)

# 合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]
print(list1)  # [400, 1, 3, 5, 7, 100, 222, 1000, 2000]
print(len(list1))  # 9

# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1)  # [400, 1, 5, 7, 100, 222, 1000, 2000]

# 从指定的位置删除元素
# list1.pop(0)
print("list1.pop(0):", list1.pop(0))  # 400
print("list1:", list1)  # [1, 5, 7, 100, 222, 1000, 2000]
print("len(list1):", len(list1))  # 7
list1.pop(len(list1) - 1)
print(list1)  # [1, 5, 7, 100, 222, 1000]

# 清空列表元素
list1.clear()
print(list1)
