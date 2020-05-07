# -*- coding: utf-8 -*-
# @Time    : 2020/5/6
# @Author  : Edrain
"""
35. 搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        漏考虑：
        1、边界值
        2、len(list) = 0 or 1 的情况
        :param nums:
        :param target:
        :return:
        """
        l_nums = len(nums)
        for i in range(l_nums):
            if nums[i] == target:
                return i
        if l_nums == 1:
            if nums[0] > target:
                return 0
            else:
                return 1
        elif l_nums == 0:
            return 0
        for i in range(1, l_nums):
            if l_nums > 1:
                if nums[i - 1] < target < nums[i]:
                    return i
                elif nums[0] > target:
                    return 0
                elif nums[l_nums - 1] < target:
                    return l_nums

    def ss01(self, nums: List[int], target: int) -> int:
        """遍历"""
        i = 0
        while i < len(nums):
            if nums[i] < target:
                i += 1
            else:
                break
        return i

    def ss02(self, nums: List[int], target: int) -> int:
        """二分法"""
        size = len(nums)
        if size == 0:
            return 0
        # 特判
        if nums[size - 1] < target:
            return size
        left = 0
        right = size - 1
        while left < right:
            mid = left + (right - left) // 2
            # 严格小于 target 的元素一定不是解
            if nums[mid] < target:
                # 下一轮搜索区间是 [mid + 1, right]
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    s = Solution()
    param1 = [1, 3, 5, 6]
    param2 = 2
    # print(s.searchInsert(param1, param2))
    print(s.ss02(param1, param2))
