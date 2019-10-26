# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 
# @Author  : Edrain


class Cat:

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")

print("that's new一个对象和赋值的区别")
# 无括号，表示这是一个类，可以用它调用类方法和静态方法，也可以把赋值给其他的变量；
tom = Cat
print("this is cat", id(Cat), Cat)
print("this is tom", id(tom),tom)
print('-' * 50)
# 带括号，Cat()表示创建一个Cat对象，可以调用他的对象方法；
tom = Cat()
print("this is cat", id(Cat), Cat)
print("this is cat()", id(Cat()), Cat())
print("this is tom", id(tom),tom)
# tom.eat()
# tom = Cat()
# tom.eat()
# tom.drink()
