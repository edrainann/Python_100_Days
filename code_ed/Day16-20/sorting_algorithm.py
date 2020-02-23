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
    选择排序存在一个明显的问题，就是它的【不稳定性】。当数列包含多个相等的元素时，选择排序有可能打乱他们的原有顺序。
    """
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
        print(f'这是{i + 1}趟', items)
    return items


def bubble_sort(origin_items, comp=lambda x, y: x > y):
    """高质量冒泡排序（搅拌排序）
    虽然存在一定的性能缺陷，却是一个稳定排序。
    所以说算法没有绝对的好坏之分，关键要看应用场景。
    """
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


def bubble_sort_01(origin_items):
    """
    简单的冒泡排序-正序
    https://www.runoob.com/w3cnote/bubble-sort.html
    比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
    """
    for i in range(1, len(origin_items)):
        print("this is i:", i)
        for j in range(0, len(origin_items) - i):
            print("j:", j)
            if origin_items[j] > origin_items[j + 1]:
                origin_items[j], origin_items[j + 1] = origin_items[j + 1], origin_items[j]
    return origin_items


def bubble_sort_02(origin_items):
    """简单的冒泡排序-倒序"""
    for i in range(1, len(origin_items)):
        for j in range(0, len(origin_items) - i):
            if origin_items[j] < origin_items[j + 1]:
                origin_items[j], origin_items[j + 1] = origin_items[j + 1], origin_items[j]
    return origin_items


def selection_sort_01(origin_items):
    """选择排序-正序
    https://www.runoob.com/w3cnote/selection-sort.html
    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
    再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    重复第二步，直到所有元素均排序完毕。
    """
    for i in range(len(origin_items) - 1):
        min_index = i  # 记录最小数的索引
        for j in range(i + 1, len(origin_items)):
            if origin_items[j] < origin_items[min_index]:
                min_index = j
        if i != min_index:  # i 不是最小数时，将 i 和最小数进行交换
            origin_items[i], origin_items[min_index] = origin_items[min_index], origin_items[i]
            print(f'第{i + 1}趟，值为{origin_items}')
    return origin_items


def selection_sort_02(origin_items):
    """选择排序-倒序"""
    for i in range(len(origin_items) - 1):
        max_index = i
        for j in range(i + 1, len(origin_items)):
            if origin_items[j] > origin_items[max_index]:
                max_index = j
        if i != max_index:
            origin_items[i], origin_items[max_index] = origin_items[max_index], origin_items[i]
    return origin_items


if __name__ == '__main__':
    items = [11, 9, 2, 4]
    ss = selection_sort_02(items)
    print(ss)
