# -*- coding: utf-8 -*-
# @Time    : 2020/5/5
# @Author  : Edrain
"""
28. 实现 strStr()

实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_l = list(haystack)
        needle_l = list(needle)
        nums = 0
        if len(needle_l) == 0:
            return 0
        elif len(needle_l) == 1:
            while nums < len(haystack_l):
                if haystack_l[nums] != needle_l[0]:
                    nums += 1
                else:
                    return nums
        for i in range(0, len(needle)-1):
            for j in range(0, len(haystack)-1):
                while nums < len(needle_l) - i:
                    if needle_l[i+nums] != haystack_l[j+nums]:
                        nums += 1
                    else:
                        nums += 0
                        break
                return j
        if nums == 0:
            return -1


if __name__ == '__main__':
    s = Solution()
    param1 = "bcaaa"
    param2 = "aaa"
    print(s.strStr(param1, param2))
