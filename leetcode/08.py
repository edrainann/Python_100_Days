# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 
# @Author  : Edrain
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #1 反转 2判断是否相等 3负数
        if x >= 0:
            new_x01 = str(x)
            new_x02 = new_x01[::-1]
            return True if new_x01 == new_x02 else False
        else:
            return False

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
