# -*- coding: utf-8 -*-
# @Time    : 2020/5/4
# @Author  : Edrain
"""
26. 删除排序数组中的重复项

给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

 

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
 

说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """通过for删除重复元素"""
        length = len(nums)
        i = 0
        for j in range(1, length):
            if i == length:
                return len(nums)
            elif nums[i] != nums[i + 1]:
                i = i + 1
            else:
                del nums[i]
                length = length - 1
        return len(nums)

    def rd02(self, nums: List[int]) -> int:
        """while删除重复元素"""
        i = 1
        # while i <= len(nums) - 1:
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                del nums[i]
            else:
                i += 1
        return len(nums)

    def rd03(self, nums: List[int]) -> int:
        """错误的！！！
        while删除重复元素
        if nums[i] == nums[i+1]:
        IndexError: list index out of range
        """
        i = 0
        while i < len(nums):
            if nums[i] == nums[i + 1]:
                del nums[i]
            else:
                i += 1
        return len(nums)

    def rd04(self, nums: List[int]) -> int:
        """通过for删除重复元素"""
        length = len(nums)
        i = 1
        for j in range(1, length):
            if nums[i - 1] != nums[i]:
                i = i + 1
            else:
                del nums[i]
                length = length - 1
        return len(nums)

    def rd05(self, nums: List[int]) -> int:
        """指针法
        构造指针保留最后一个不重复的元素，遍历过程对比元素，如果不同，则覆写
        """
        flag = 0
        if len(nums) == 0:
            return flag
        for i in range(1, len(nums)):
            if nums[i] != nums[flag]:
                flag += 1
                nums[flag] = nums[i]
        return flag+1


if __name__ == '__main__':
    s = Solution()
    # params = [1, 1, 1]
    params = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # print(s.removeDuplicates(params))
    print(s.rd05(params))
