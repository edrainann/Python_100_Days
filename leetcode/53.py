# -*- coding: utf-8 -*-
# @Time    : 2020/5/10
# @Author  : Edrain
"""
53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """不得行，人家可能多个连着才最大"""
        n = len(nums)
        sum_nums = 0
        new_list = []
        i = 0
        j = 0
        while i < n:
            while j < n - i - 1:
                sum_nums += nums[j]
                if sum_nums > sum_nums + nums[j + 1]:
                    new_list.append(sum_nums)
                    sum_nums = 0
                    break
                else:
                    j += 1
            i += 1
            j = i
        print(new_list)
        return max(new_list)

    def maxSubArray01(self, nums: List[int]) -> int:
        """开始尝试暴力破解了
        喔豁--好不容易实现了---结果超出时间限制"""
        n = len(nums)
        sum_nums = 0
        new_list = []
        i = 0
        j = 0
        while i < n:
            while j < n:
                sum_nums += nums[j]
                new_list.append(sum_nums)
                j += 1
            i += 1
            j = i
            sum_nums = 0
        return max(new_list)

    def maxSubArray02(self, nums: List[int]) -> int:
        """链接：https://leetcode-cn.com/problems/maximum-subarray/solution/bao-li-qiu-jie-by-pandawakaka/"""
        tmp = nums[0]
        max_ = tmp
        n = len(nums)
        for i in range(1, n):
            # 当当前序列加上此时的元素的值大于tmp的值，说明最大序列和可能出现在后续序列中，记录此时的最大值
            if tmp + nums[i] > nums[i]:
                max_ = max(max_, tmp + nums[i])
                tmp = tmp + nums[i]
            else:
                # 当tmp(当前和)小于下一个元素时，当前最长序列到此为止。以该元素为起点继续找最大子序列,
                # 并记录此时的最大值
                max_ = max(max_, tmp, tmp + nums[i], nums[i])
                tmp = nums[i]
        return max_

    def maxSubArray03(self, nums: List[int]) -> int:
        """分治法
        它的最大子序和要么在左半边，要么在右半边，要么是穿过中间，对于左右边的序列，情况也是一样，因此可以用递归处理。
        中间部分的则可以直接计算出来，时间复杂度应该是 O(nlogn)O(nlogn)。
        """
        n = len(nums)
        # 递归终止条件
        if n == 1:
            return nums[0]
        else:
            # 递归计算左半边最大子序和
            max_left = self.maxSubArray(nums[0:len(nums) // 2])
            # 递归计算右半边最大子序和
            max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])

        # 计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        # 返回三个中的最大值
        return max(max_right, max_left, max_l + max_r)

    def maxSubArray04(self, nums: List[int]) -> int:
        """
        核心问题：滚动加总是不是整数
        One-pass 时间复杂度是O(N)
        是整数，就继续加总，因为整数就是增加的基础
        是负数，就可以开始新的滚动加总了。
        每一步都比较一下max
        没有使用max()函数，好像能快点？
        链接：https://leetcode-cn.com/problems/maximum-subarray/solution/python-5xing-jian-hua-wen-ti-he-ji-shu-shi-fou-da-/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""
        max_, sum_ = nums[0], nums[0]
        for n in nums[1:]:
            sum_ = sum_ + n if sum_ >= 0 else n
            max_ = max_ if max_ > sum_ else sum_  # 比max快点?
        return max_


if __name__ == '__main__':
    s = Solution()
    param1 = [-2, -1, -3, 4, -1, -2, -1, -5, -4]
    # print(s.maxSubArray(param1))
    print(s.maxSubArray04(param1))
