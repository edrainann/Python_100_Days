#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11
# @Author  : Edrain
"""
在Python中可以使用class关键字定义类，然后在类中通过之前学习过的函数来定义方法，这样就可以将对象的动态特征描述出来
写在类中的函数，我们通常称之为（对象的）方法，这些方法就是对象可以接收的消息。
"""


class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print(f'{self.name}只能观看少儿节目')
        else:
            print(f'{self.name}正在观看大于18岁可以观看的节目')


def main():
    """当我们定义好一个类之后，可以通过下面的方式来创建对象并给对象发消息。"""
    stu1 = Student('ed', 68)
    stu1.study('好玩的课程')
    stu1.watch_movie()
    stu2 = Student('红红', 11)
    stu2.study('小学课程')
    stu2.watch_movie()


if __name__ == '__main__':
    main()
