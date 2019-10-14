#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12
# @Author  : Edrain
"""
子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，这个动作称之为方法重写（override）。
通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，
当我们调用这个经过子类重写的方法时，不同的子类对象会表现出不同的行为，这个就是多态（poly-morphism）。
"""
from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音
        将Pet类处理成了一个抽象类，所谓抽象类就是不能够创建对象的类，这种类的存在就是专门为了让其他类去继承它。
        Python从语法层面并没有像Java或C#那样提供对抽象类的支持，
        但是我们可以通过abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类的效果，
        如果一个类中存在抽象方法那么这个类就不能够实例化（创建对象）。
        """
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print(f'{self._nickname}:汪汪汪...')


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print(f'{self._nickname}:喵...喵...')


def main():
    pets = [Dog('旺财'), Cat('喵咪'), Dog('来福')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
