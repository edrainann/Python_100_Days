# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 
# @Author  : Edrain
import random


class RandomDemo(object):
    def random_demo_01(self):
        """python生成100个不重复的4位数随机数。"""
        nums = ""
        for i in range(10):
            a = random.randint(111, 333)
            str_a = f"{a}\n"
            nums += str_a
        return nums

    def random_demo_02(self):
        nums = random.sample(range(1000, 9999), 10)
        return nums

    def random_demo_03(self):
        nums = []
        # for _ in range(10):
        while True:
            a = random.randint(1000, 9999)
            if a not in nums:
                nums.append(a)
            if len(nums) == 100:
                break
        return nums


if __name__ == '__main__':
    r = RandomDemo()
    # print(r.random_demo_01())
    # print(r.random_demo_02())
    print(r.random_demo_03())
