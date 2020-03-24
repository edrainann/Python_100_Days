# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 
# @Author  : Edrain
from typing import List


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:] = sorted(nums1[:m] + nums2)

    def merge_01(self, nums1, m, nums2, n):
        nums1[m:m + n] = nums2
        return nums1.sort()

    def merge_02(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # sort()方法实现
        if nums1 is None or nums2 is None:
            return nums1
        nums1[m:m + n] = nums2
        return nums1.sort()

    def merge_03(self, nums1, m, nums2, n):
        for i in range(len(nums1) - 1, m - 1, n - 1):
            del nums1[i]
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        return nums1.sort()


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3
    print(Solution().merge(nums1, 1, nums2, 0))
    print(s.merge_01(nums1, m, nums2, n))
    print(s.merge_02(nums1, m, nums2, n))
    print(s.merge_03(nums1, m, nums2, n))
