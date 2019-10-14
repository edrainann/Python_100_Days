#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11
# @Author  : Edrain


set1 = {1, 2, 3, 3, 2}
print(set1)  # {1, 2, 3}
print('Length=', len(set1))  # Length= 3

set2 = set(range(1, 10))
print(set2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

set1.add(4)
set1.add(5)
print(set1)  # {1, 2, 3, 4, 5}

set2.update([11, 12])
print(set2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}

set2.discard(11)
print("set2.discard(11):", set2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 12}

if 4 in set2:
    set2.remove(4)
print(set2)  # {1, 2, 3, 5, 6, 7, 8, 9, 12}

for elem in set2:
    print("elem**2:", elem ** 2,
          end='       ')  # elem**2: 1       elem**2: 4       elem**2: 9       elem**2: 25       elem**2: 36       elem**2: 49       elem**2: 64       elem**2: 81       elem**2: 144       --------
print("--------")

# 将元组转换成集合
# set3 = set((1, 2, 3, 3, 2, 1))
set3 = {1, 2, 3, 3, 2, 1}
print(set3.pop())  # 1
print(set3)  # {2, 3}

# 集合的交集、并集、差集、对称差运算
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))

# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))
