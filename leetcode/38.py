# -*- coding: utf-8 -*-
# @Time    : 2020/5/10
# @Author  : Edrain
"""
38. 外观数列

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

注意：整数序列中的每一项将表示为一个字符串。

 

示例 1:

输入: 1
输出: "1"
解释：这是一个基本样例。
示例 2:

输入: 4
输出: "1211"
解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；类似 "1" 可以读作 "11"。所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-and-say
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        """嗷嗷嗷 没有想出来啊
        递归递归！！！"""
        i = 3
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        else:
            while i <= n:
                pass

    def countAndSay01(self, n: int) -> str:
        """
        循环含义
        每次外循环含义为给定上一个人报的数，求下一个人报的数
        每次内循环为遍历上一个人报的数
        具体思路
        先设置上一人为'1'
        开始外循环
        每次外循环先置下一人为空字符串，置待处理的字符num为上一人的第一位，置记录出现的次数为1
        开始内循环，遍历上一人的数，如果数是和num一致，则count增加。
        若不一致，则将count和num一同添加到next_person报的数中，同时更新num和count
        别忘了更新next_person的最后两个数为上一个人最后一个字符以及其出现次数！
        链接：https://leetcode-cn.com/problems/count-and-say/solution/ji-su-jie-bu-di-gui-zhi-ji-lu-qian-hou-liang-ren-p/
        """
        prev_person = '1'
        for i in range(1, n):
            next_person, num, count = '', prev_person[0], 1
            for j in range(1, len(prev_person)):
                if prev_person[j] == num:
                    count += 1
                else:
                    next_person += str(count) + num
                    num = prev_person[j]
                    count = 1
            next_person += str(count) + num
            prev_person = next_person
        return prev_person

    def countAndSay02(self, n: int) -> str:
        seq = '1'
        for i in range(n - 1):
            seq = self.getNext(seq)
        return seq

    def getNext(self, seq):
        i, next_seq = 0, ""
        while i < len(seq):
            count = 1
            while i < len(seq) - 1 and seq[i] == seq[i + 1]:
                count += 1
                i += 1
            next_seq += str(count) + seq[i]
            i += 1
        return next_seq

    def countAndSay03(self, n: int) -> str:
        """
        使用递归的方法
        这道题其实跟斐波那契数列有点类似，都是基于上一项的结果得出下一项的结果，因此适合使用递归来解决问题。
        因为确定了n=1时的值，所以基线条件就可以设置为 n <= 1 时返回。
        在后面的循环里，思路是当遇到的字符串与上一个相等的时候，计数器+1，否则结束计数，并将当前结果添加到res变量中，并且计数器恢复到1。
        比较需要注意的是边际条件，在字符串开头跟结尾的时候做了单独的处理。
        链接：https://leetcode-cn.com/problems/count-and-say/solution/python3-di-gui-fa-jie-wai-guan-shu-lie-by-mmmz/
        """
        if n <= 1:
            return '1'
        pre = self.countAndSay(n - 1)

        res = ''
        count = 1
        for idx in range(len(pre)):

            # 处理字符串开头的时候
            if idx == 0:
                count = 1

            elif pre[idx] != pre[idx - 1]:
                tmp = str(count) + pre[idx - 1]
                res += tmp
                count = 1
            elif pre[idx] == pre[idx - 1]:
                count += 1

            # 处理字符串末尾的时候
            if idx == len(pre) - 1:
                tmp = str(count) + pre[idx]
                res += tmp
        return res


if __name__ == '__main__':
    s = Solution()
    param = 6
    print(s.countAndSay01(param))
