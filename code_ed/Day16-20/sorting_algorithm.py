#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23
# @Author  : Edrain
"""
排序算法（选择、冒泡和归并）和查找算法（顺序和折半）
"""


def select_sort(origin_items, comp=lambda x, y: x < y):
    """简单选择排序
    选择排序的核心：每一轮比较找到一个极值（最大值或最小值）放到某一端，对剩下的数再找极值，直至比较结束。
    操作方法：
    第一趟，从n 个记录中找出关键码最小的记录与第一个记录交换；
    第二趟，从第二个记录开始的n-1 个记录中再选出关键码最小的记录与第二个记录交换；
    ......
    第 i 趟，则从第 i 个记录开始的 n-i+1 个记录中选出关键码最小的记录与第 i 个记录交换，直到整个序列按关键码有序
    初始值：11 9 2 4
    第一趟：2 11 9 4
    第二趟：2 4 11 9
    第三趟：2 4 9 11
    """
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
        print(f'这是{i+1}趟', items)
    return items


if __name__ == '__main__':
    ss = select_sort([11, 9, 2, 4])
    print(ss)
