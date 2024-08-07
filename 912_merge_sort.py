# -*- coding: utf-8 -*-
"""
@Time ： 2024/8/7 下午2:35
@Auth ： simonzfei
@File ：912_merge_sort.py
@IDE ：PyCharm
@Motto：thinking coding 
"""

## merge_sort
class Solution(object):
    def sortArray(self, nums):
        nums = self.merge_sort(nums)
        print(nums)

    def merge(self, left_nums: [int], right_nums: [int]):
        nums = []
        left_i, right_j = 0, 0
        while left_i < len(left_nums) and right_j < len(right_nums):
            if left_nums[left_i] < right_nums[right_j]:
                nums.append(left_nums[left_i])
                left_i += 1
            else:
                nums.append(right_nums[right_j])
                right_j += 1
        while left_i < len(left_nums):
            nums.append(left_nums[left_i])
            left_i += 1
        while right_j < len(right_nums):
            nums.append(right_nums[right_j])
            right_j += 1
        return nums

    def merge_sort(self, nums: [int]) -> [int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left_nums = self.merge_sort(nums[0: mid])
        right_nums = self.merge_sort(nums[mid:])
        return self.merge(left_nums, right_nums)


nums = [5, 1, 1, 2, 0, 0]
Solution().sortArray(nums=nums)
