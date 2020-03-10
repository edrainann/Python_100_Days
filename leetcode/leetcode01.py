# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 
# @Author  : Edrain
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转
"""


def reverse_force(x: int) -> int:
    """暴力解法"""
    if -10 < x < 10:
        return x
    str_x = str(x)
    if str_x[0] != "-":
        str_x = str_x[::-1]
        x = int(str_x)
    else:
        str_x = str_x[:0:-1]
        x = int(str_x)
        x = -x
    return x if -2147483648 < x < 2147483647 else 0


def reverse_01(x):
    """通过list.reverse进行list的反转"""
    print(x)
    x.reverse()
    return x


if __name__ == '__main__':
    a = 1233222
    b = [1, 2, 3]
    c = "123456"
    print(reverse_force(a))
    print(reverse_01(b))
    list_01 = [1, 2, 3, 4]
    list_01.reverse()
    print(list_01)
    print(c[::-1])  # 切片
