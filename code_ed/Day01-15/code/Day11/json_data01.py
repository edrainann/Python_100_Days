# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 
# @Author  : Edrain
"""
使用Python中的json模块就可以将字典或列表以JSON格式保存到文件中
json模块主要有四个比较重要的函数，分别是：
dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象
这里出现了两个概念，一个叫序列化，一个叫反序列化。
自由的百科全书维基百科上对这两个概念是这样解释的：
“序列化（serialization）在计算机科学的数据处理中，是指将数据结构或对象状态转换为可以存储或传输的形式，
这样在需要的时候能够恢复到原先的状态，而且通过序列化的数据重新获取字节时，可以利用这些字节来产生原始对象的副本（拷贝）。
与这个过程相反的动作，即从一系列字节中提取数据结构的操作，就是反序列化（deserialization）”。
"""
import json


def main():
    my_dict = {
        'name': '哇哈哈',
        'age': 88,
        'qq': 666888,
        'friends': ['哇有才', '哈有福'],
        'cars': [
            {'brand': 'Fen', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(my_dict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    main()