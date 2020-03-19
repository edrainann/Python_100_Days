# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 
# @Author  : Edrain
"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        # 1分布读取出来 2从头开始找相同
        global same
        if len(strs) - 1 == 0:
            return str(strs[0])
        else:
            for i in range(len(strs) - 1):
                same = ""
                list_s_i = strs[i]
                choose = len(strs[i]) if len(strs[i]) <= len(strs[i + 1]) else len(strs[i + 1])
                for j in range(choose):
                    if list_s_i[j] != strs[i + 1][j]:
                        break
                    else:
                        same = same + list_s_i[j]
                strs.pop(i)
                strs.insert(i + 1, same)
                # print(strs)
            return same


if __name__ == '__main__':
    s = Solution()
    # a = ["flower", "flow", "flight"]
    a = ["f"]
    print(s.longestCommonPrefix(a))
