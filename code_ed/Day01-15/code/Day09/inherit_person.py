#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12
# @Author  : Edrain
"""
继承和多态
刚才我们提到了，可以在已有类的基础上创建新类，这其中的一种做法就是让一个类从另一个类那里将属性和方法直接继承下来，
从而减少重复代码的编写。
提供继承信息的我们称之为父类，也叫超类或基类；
得到继承信息的我们称之为子类，也叫派生类或衍生类。
子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力，
在实际开发中，我们经常会用子类对象去替换掉一个父类对象，这是面向对象编程中一个常见的行为，对应的原则称之为里氏替换原则。
下面我们先看一个继承的例子。
"""


class Person(object):
    """人"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print(f'{self._name}正在愉快的玩耍---哈哈哈哈')

    def watch_movie(self):
        if self._age >= 18:
            print(f'{self._name}正在看动画片')
        else:
            print(f"{self._name}就只能好好写作业了")


class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print(f'{self._grade}的{self._name}正在学习{course}')


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print(f'{self._name} {self._title} 正在讲{course}')


def main():
    stu = Student('哇哈哈', 86, '小学')
    stu.study("高数")
    stu.watch_movie()
    t = Teacher('哇哈哈老师', 800, "超级厉害")
    t.teach('灰常难的一门学课')
    t.watch_movie()


if __name__ == '__main__':
    main()
