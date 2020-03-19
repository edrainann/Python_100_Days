# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 
# @Author  : Edrain
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""
class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(abs(x))
        str_new_x = str_x[::-1]
        if x < 0:
            new_x = int(str_new_x)
            new_x = -new_x
            # new_x = int("-"+new_x)
        else:
            new_x = int(str_new_x)
        # return new_x if -(1<<31) < x < (1<<31)-1 else 0
        return new_x if -2147483648 < new_x < 2147483647 else 0  # 输出溢出检查


if __name__ == '__main__':
    s = Solution()
    a = 1534236469
    if -2147483648 < a < 2147483647:
        print("ok")
    else:
        print("no")
    print(s.reverse(a))
    print(-(1 << 31))
    print((1 << 31) - 1)
    print(len('123'))
    list = [1,2,3]
    print(list.pop(-2))