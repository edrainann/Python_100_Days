#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28
# @Author  : Edrain


class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("没有子弹了...")
            return
        self.bullet_count -= 1
        print(f'{self.model}发射子弹{self.bullet_count}')


# # 创建枪对象
# ak47 = Gun("ak47")
# ak47.add_bullet(5)
# ak47.shoot()

class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:
            print(f'嗷嗷嗷 {self.name}还没有枪...')
            return
        print(f'冲鸭鸭....【{self.name}】')
        self.gun.add_bullet(8)  # 让枪装上子弹
        self.gun.shoot()  # 让枪发射子弹


ak47 = Gun("AK47")
wah = Soldier("哇哈哈")
wah.gun = ak47  # 创建对象，让对象调用方法
wah.fire()
