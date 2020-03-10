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


def reverse(x: int) -> int:
    """
    算法思路： 为对当前数取对 1010 的余数，再一项项填入res尾部，即可完成 intint 翻转。
    边界情况处理： int 取值范围为 [-2^{31}, 2^{31} - 1]，如果翻转数字溢出，则立即返回 00 。
    Python： 存储数字理论上是无限长度，因此每次计算完后判断res与of的大小关系即可；
    Java： 数字计算会溢出，因此要判断res和of / 10的大小关系（即确定再添 11 位是否会溢出）。
    Python的坑： 由于Python的 // 操作是向下取整，导致正负数取余 % 操作结果不一致，因此需要将原数字转为正数操作。
    链接：https://leetcode-cn.com/problems/reverse-integer/solution/reverse-integer-by-jin407891080/
    """
    y, res = abs(x), 0
    of = (1 << 31) - 1 if x > 0 else 1 << 31
    while y != 0:
        res = res * 10 + y % 10
        if res > of:
            return 0
        y //= 10
    return res if x > 0 else -res


def reverse_01(x):
    """通过list.reverse进行list的反转"""
    print(x)
    x.reverse()
    return x


if __name__ == '__main__':
    a = -123
    b = [1, 2, 3]
    c = "123456"
    print(reverse_force(a))
    print(reverse_01(b))
    list_01 = [1, 2, 3, 4]
    list_01.reverse()
    print(list_01)
    print(c[::-1])  # 切片
    print(reverse(a))
