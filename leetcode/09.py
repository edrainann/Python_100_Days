# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 
# @Author  : Edrain
"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 1 反转 2判断是否相等 3负数
        if x >= 0:
            new_x01 = str(x)
            new_x02 = new_x01[::-1]
            return True if new_x01 == new_x02 else False
        else:
            return False

    def isPalindrome02(self, x: int) -> bool:
        str_new_x = str(x)
        new_x = list(str_new_x)
        if len(new_x) == 1:
            return True
        for i in range(len(new_x)):
            if new_x[i] != new_x[-i - 1]:
                return False
        return True

    def isPalindrome03(self, x: int) -> bool:
        lst = list(str(x))
        while len(lst) > 1:
            if lst.pop(0) != lst.pop():
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    a = 1000021
    print(s.isPalindrome02(a))
