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
        """错误解法
        没有想出如何解答"""
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
        for i in range(0, len(needle) - 1):
            for j in range(0, len(haystack) - 1):
                while nums < len(needle_l) - i and nums < len(haystack_l) - j:
                    if needle_l[i + nums] != haystack_l[j + nums]:
                        nums += 1
                    else:
                        nums += 0
                        break
                return nums
        if nums == 0:
            return -1

    def ss01(self, haystack: str, needle: str) -> int:
        try:
            bb = haystack.index(needle)
            return bb
        except ValueError:
            return -1

    def ss02(self, haystack: str, needle: str) -> int:
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(needle)
        for i in range(len(haystack) - m + 1):
            if haystack[i:m + i] == needle:
                return i
        return -1

    def ss03(self, haystack: str, needle: str) -> int:
        lh = len(haystack)
        ln = len(needle)

        if ln == 0:
            return 0
        if lh == 0 or lh < ln:
            return -1
        i = 0
        while i <= lh - ln:
            if haystack[i] == needle[0]:
                if haystack[i:i + ln] == needle:
                    return i
                else:
                    i = i + 1
            else:
                i += 1
        return -1

    def ss04(self, haystack: str, needle: str) -> int:
        """看完其余解体思路后，修改之前代码，最终成功"""
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
            return -1
        for i in range(0, len(haystack) - 1):
            if haystack_l[i] == needle_l[0]:
                # while nums < len(needle_l) and nums < len(haystack_l):
                if haystack_l[i:i + len(needle_l)] == needle_l:
                    return i
        if nums == 0:
            return -1

    def ss05(self, haystack: str, needle: str) -> int:
        """看完其余解体思路后，修改之前代码，最终成功了，但是执行效率不高"""
        haystack_l = list(haystack)
        needle_l = list(needle)
        if len(needle_l) == 0:
            return 0
        if len(haystack_l) == 0 or len(haystack_l) < len(needle_l):
            return -1
        for i in range(0, len(haystack)):
            if haystack_l[i] == needle_l[0]:
                if haystack_l[i:i + len(needle_l)] == needle_l:
                    return i
        return -1

    def ss06(self, haystack: str, needle: str) -> int:
        """优化代码成功,会比第一种执行用时更短"""
        l_haystack = len(haystack)
        l_needle = len(needle)
        if l_needle == 0:
            return 0
        if l_haystack == 0 or l_haystack < l_needle:
            return -1
        for i in range(0, len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i + l_needle] == needle:
                    return i
        return -1


if __name__ == '__main__':
    s = Solution()
    param1 = "f"
    param2 = "f"
    # print(s.strStr(param1, param2))
    print(s.ss05(param1, param2))
