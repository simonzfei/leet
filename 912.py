# -*- coding: utf-8 -*-
"""
@Time ： 2024/6/22 下午4:22
@Auth ： simonzfei
@File ：912.py
@IDE ：PyCharm
@Motto：thinking coding 
"""
"""

912. 排序数组
给你一个整数数组 nums，请你将该数组升序排列

示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]

示例 2：

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]


提示：

    1 <= nums.length <= 5 * 104
    -5 * 104 <= nums[i] <= 5 * 104
"""

import random


class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        low, high = 0, len(nums)
        self.quickSort(nums, low, high-1)
        print(nums)

    # def partition(self, nums, low, high):


    def partition(self, nums, low, high):
        pivot_index = random.randint(low, high)
        nums[pivot_index], nums[high] = nums[high], nums[pivot_index]
        pivot = nums[high]
        print(pivot)
        i = low
        for j in range(low, high):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[high], nums[i] = nums[i], nums[high]
        print(nums)
        return i
    #
    def quickSort(self, nums, low, high):
        if low < high:
            pivot = self.partition(nums, low, high)
            self.quickSort(nums, low, pivot - 1)
            self.quickSort(nums, pivot + 1, high)

    #     pivot_index = random.randint(low, high)
    #     nums[pivot_index], nums[high] = nums[high], nums[pivot_index]
    #     pivot = nums[high]
    #     print(pivot)
    #     i = low - 1
    #     for j in range(low, high):
    #         if nums[j] <= pivot:
    #             i += 1
    #             nums[i], nums[j] = nums[j], nums[i]
    #     nums[i + 1], nums[high] = nums[high], nums[i + 1]
    #     print(nums)
    #     return i + 1

    # wrong
    # def quickSort(self, nums, low, high):
        # if low < high:
        #
        #     pivot = self.partition(nums, low, high)
        #     self.partition(nums, low, pivot - 1)
        #     self.partition(nums, pivot+1, high)


# nums = [5,2,3,1]
nums = [5,1,1,2,0,0,7,6,6,8]
Solution().sortArray(nums = nums)

