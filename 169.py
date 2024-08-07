# -*- coding: utf-8 -*-
"""
@Time ： 2024/8/7 下午3:35
@Auth ： simonzfei
@File ：169.py
@IDE ：PyCharm
@Motto：thinking coding 
"""

"""
169. 多数元素
简单
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：
输入：nums = [3,2,3]
输出：3

示例 2：
输入：nums = [2,2,1,1,1,2,2]
输出：2

提示：

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109

 

进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。

"""

import random

## quick sort time out
# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         high = len(nums)-1
#         self.quickSort(nums, 0, high)
#
#         print(nums)
#         return nums[len(nums)//2]
#
#
#
#
#     def partition(self, nums, low, high):
#         i = random.randint(low, high)
#         nums[i], nums[low] = nums[low], nums[i]
#
#
#         pivot = nums[low]
#         i, j = low, high
#         while i < j:
#             while i < j and nums[j] >= pivot:
#                 j -= 1
#             while i < j and nums[i] <= pivot:
#                 i += 1
#             nums[i], nums[j] = nums[j], nums[i]
#
#         nums[i], nums[low] = nums[low], nums[i]
#         return i
#
#     def quickSort(self, nums, low, high):
#
#         if low < high:
#             pivot_i = self.partition(nums, low, high)
#             self.quickSort(nums, low, pivot_i - 1)
#             self.quickSort(nums, pivot_i + 1, high)
#         return nums


#Boyer-Moore Voting Algorithm
# O(N)
class Solution(object):
    def majorityElement(self, nums: [int]):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        print(candidate)

nums = [2, 2, 1, 1, 1, 2, 2]
Solution().majorityElement(nums=nums)
