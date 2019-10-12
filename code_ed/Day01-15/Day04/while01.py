#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8
# @Author  : Edrain
"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
import random


answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input("请输入一个猜测的数字："))
    if number > answer:
        print("请输入 小一点的")
    elif number < answer:
        print("请输入 大一点的")
    else:
        print("恭喜您，猜对了！")
        break
print("您总共猜了{}次".format(counter))
if counter > 7:
    print("您的猜测次数有点多了哟")
