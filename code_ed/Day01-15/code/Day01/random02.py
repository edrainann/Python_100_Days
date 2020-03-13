# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 
# @Author  : Edrain
import random

lsGiftIn = [['Jack', 'apple'], ['June', 'ball'], ['Mary', 'card'], ['Duke', 'doll'], ['James', 'egg'],
            ['Tina', 'flute'], ['Tom', 'coffee']]  # 存储参与者的姓名和自己带来的礼物
lsGiftOut = []  # 存储交换后的结果
n = len(lsGiftIn)  # 参与人数
gifts = [i[1] for i in lsGiftIn]  # 未分配出去的礼物
for x in range(n):
    flag = 0
    person = lsGiftIn[x][0]
    myGift = lsGiftIn[x][1]
    if myGift in gifts:
        flag = 1
        gifts.remove(myGift)
    getGift = random.choice(gifts)  # 随机分配礼物
    lsGiftOut.append([person, getGift])
    gifts.remove(getGift)
    if flag:
        gifts.append(myGift)

print(lsGiftOut)