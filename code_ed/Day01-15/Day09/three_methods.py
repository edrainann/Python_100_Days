#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12
# @Author  : Edrain


print("----------实例方法--------------")


class KlsInstance(object):
    """实例方法"""

    def __init__(self, data):
        self.date = data

    def printd(self):
        """printd为一个实例方法。
        实例方法第一个参数为self，当使用ik1.printd()调用实例方法时，实例ik1会传递给self参数，
        这样self参数就可以引用当前正在调用实例方法的实例。
        利用实例方法的这个特性，上述代码正确输出了两个实例的成员数据。"""
        print(self.date)


ik1 = KlsInstance('ooo')
ik2 = KlsInstance('eee')

ik1.printd()
ik2.printd()

print("----------类方法-------------")


class KlsClass(object):
    """我们需要统计类Kls实例的个数，因此定义了一个类变量num_inst来存放实例个数。
    通过装饰器@classmethod的使用，方法get_no_of_instance被定义成一个类方法。
    在调用类方法时，Python 会将类（class Kls）传递给cls，这样在get_no_of_instance内部就可以引用类变量num_inst。
    由于在调用类方法时，只需要将类型本身传递给类方法，因此，既可以通过类也可以通过实例来调用类方法"""
    num_inst = 0

    def __init__(self):
        KlsClass.num_inst = KlsClass.num_inst + 1

    @classmethod
    def get_no_of_instance(cls):
        return cls.num_inst


ik1 = KlsClass()
ik2 = KlsClass()
print(ik1.get_no_of_instance())
print(KlsClass.get_no_of_instance())

print("----------静态方法-----------")
IND = 'ON'


class KlsStatic(object):
    """静态方法
    在开发中，我们常常需要定义一些方法，这些方法跟类有关，但在实现时并不需要引用类或者实例，
    例如，设置环境变量，修改另一个类的变量，等。这个时候，我们可以使用静态方法。
    Python 使用装饰器@staticmethod来定义一个静态方法。"""

    def __init__(self, date):
        self.date = date

    @staticmethod
    def checkind():
        return IND == 'ON'

    def do_reset(self):
        if self.checkind():
            print('Reset done for: %s' % self.date)

    def set_db(self):
        if self.checkind():
            print('DB connection made for: %s' % self.date)


ik1 = KlsStatic(22)
ik1.do_reset()
ik1.set_db()


class Province(object):
    """
    类对象只有一个，可以通过类对象创建n个实例对象
    类对象：公有的
    实例属性：私有的
    """

    # 类属性
    country = '中国'

    def __init__(self, name):
        # 实例属性
        self.name = name

    def class_fun(self):
        print("----------实例方法啊---------")

    @staticmethod
    def static_fun():
        print('=========静态方法哟==========')


# 创建一个实例对象
obj = Province('重庆市')
# 直接访问实例属性
print(obj.name)
# 直接访问属性
print("Province.country", Province.country)
# print("Province.class_fun", Province.class_fun())  # Parameter 'self' unfilled 类对象无法调用实例方法
print("实例对象调用 类属性-->", obj.country)  # 实例对象调用 类属性
# print("实例对象调用 类属性-->",obj.country='wawa')  # Can't assign to function call
obj.__class__.country = 'waa'
print("实例对象调用 类属性-->", obj.country)  # 实例对象修改类属性

obj.class_fun()  # 实例对象调用 实例方法
print(obj.name)  # 实例对象调用 实例属性
obj.static_fun()  # 实例对象调用 静态方法


class Foo(object):
    def __init__(self, name):
        self.name = name

    def ord_func(self):
        """定义实例方法，至少有一个self参数"""
        print(self.name)
        print('实例方法')

    @classmethod
    def class_func(cls):
        """定义类方法，至少有一个cls参数"""
        print('类方法')

    @staticmethod
    def static_func():
        """定义静态方法，无默认参数"""
        print('静态方法')


f = Foo('中国')
# 调用实例方法
f.ord_func()

# 调用类方法
Foo.class_func()

# 调用静态方法
Foo.static_func()
