#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11
# @Author  : Edrain
"""
字典是另一种可变容器模型，类似于我们生活中使用的字典，
它可以存储任意类型对象，与列表、集合不同的是，字典的每个元素都是由一个键和一个值组成的“键值对”，键和值通过冒号分开。
"""

scores = {"哇哈哈": 100,
          "小明": 88,
          "小红": 99}
# 通过键可以获取字典中对应的值
print(scores["哇哈哈"])  # 100
print('-=-=-=-=-=-=-=-=-=-=-=', scores.items())
for k in scores:
    print(f'key:{k},value:{scores[k]}')

"""
哇哈哈	---->	100
小明	---->	88
小红	---->	99
# 对字典进行遍历(遍历的其实是键再通过键取对应的值)
"""
for elem in scores:
    # print('%s\t--->\t%d' % (elem, scores[elem]))
    print(f'{elem}\t---->\t{scores[elem]}')

# 更新字典中的元素
scores["小明"] = 6666
scores["aaaa"] = 998
scores.update(bbb=67, 小黄=85)
print(scores)  # {'哇哈哈': 100, '小明': 6666, '小红': 99, 'aaaa': 998, 'bbb': 67, '小黄': 85}

if 'aoa' in scores:
    print("aoa:", scores['aoa'])
print("get_aoa:", scores.get('aoa'))

# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('a0a', 60))
print(scores)
# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
# print(scores.pop('小明'))
print(scores.pop('小明', 6666))
print(scores)
# 清空字典
scores.clear()
print(scores)
