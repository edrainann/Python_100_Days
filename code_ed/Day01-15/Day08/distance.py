#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11
# @Author  : Edrain
from math import sqrt


class Point:

    def __init__(self, x=0, y=0):
        """
        初始化方法
        :param x:横坐标
        :param y:纵坐标
        """
        self.x = x
        self.y = y
        # return self.x, self.y  # Cannot return a value from __init__

    def move_to(self, x, y):
        """
        移动到指定位置
        :param x: 新的横坐标
        :param y: 新的纵坐标
        :return:
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """
        移动指定的增量
        :param dx:横坐标的增量
        :param dy:纵坐标的增量
        :return:
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """
        计算与另一个点的距离
        :param other: 另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        distance = sqrt(dx ** 2 + dy ** 2)  # 两点间的距离公式
        return distance

    def __str__(self):
        """坐标的字符串表达式"""
        str1 = f'这是坐标：({str(self.x)},{str(self.y)})'
        # str1 = '(%s, %s)' % (str(self.x), str(self.y))
        return str1


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_to(-1, 2)
    print(p2)
    print(p1.distance_to(p2))
    p3 = Point(6, 14)
    print("p1.distance_to(p3):", p1.distance_to(p3))
    p4 = Point
    print(p4)


if __name__ == '__main__':
    main()
