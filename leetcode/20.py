# -*- coding: utf-8 -*-
# @Time    : 2020/4/29
# @Author  : Edrain
"""
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""


class Solution:
    def is_valid(self, s: str) -> bool:
        dic = {"(": ")", "{": "}", "[": "]", "?": "?"}
        stack = ["?"]
        for c in s:
            # 列出字典所有的value
            # if c in dic.values():
            # 列出字典所有的key
            # if c in dic:
            if c in dic.keys():
                stack.append(c)
                print("---", stack)
            # 字典通过key找value，dict['key']
            # 最后一项被删除的值 stack.pop()
            elif dic[stack.pop()] != c:
                print(stack)
                return False
        return len(stack) == 1

    def isValid_01(self, s: str) -> bool:
        for i in range(0, len(s) - 1):
            for j in range(1, len(s)):
                # if s[i] !=
                pass
        if s in ("()", "[]", "{}"):
            return True
        else:
            return False


if __name__ == '__main__':
    so = Solution()
    s_01 = "()"
    # print(so.isValid_01(s_01))
    s_s = "())"
    print(so.is_valid(s_s))
