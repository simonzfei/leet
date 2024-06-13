# -*- coding: utf-8 -*-
"""
@Time ： 2024/6/13 上午10:41
@Auth ： simonzfei
@File ：215.py
@IDE ：PyCharm
@Motto：thinking coding 
"""
import random

"""
 数组中的第K个最大元素
已解答
中等

给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1:
输入: [3,2,1,5,6,4], k = 2
输出: 5

示例 2:

输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
提示：
    1 <= k <= nums.length <= 105
    -104 <= nums[i] <= 104
"""
"""

# method 1:
class Solution(object):
    def findKthLargest(self, nums, k):
        nums = sorted(nums)#直接使用sorted()函数从小到大排序，区-k位置的元素
        return nums[-k]
        
"""


# 选择排序
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums) - 1):
            min_i = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_i]:
                    min_i = j
            if i != min_i:
                nums[i], nums[min_i] = nums[min_i], nums[i]
        print(nums)
        print(nums[len(nums) - k])


# 快速排序
class Solution2(object):
    def findKthLargest(self, nums, k):
        nums = self.quickSort(nums, 0, len(nums) - 1)
        print(nums[-k])
        return nums[-k]

    def randomPartition(self, nums: [int], low: int, high: int) -> int:
        i = random.randint(low, high)
        nums[i], nums[low] = nums[low], nums[i]
        return self.partition(nums, low, high)

    def partition(self, nums: [int], low: int, high: int) -> int:
        pivot = nums[low]
        i, j = low, high
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            while i < j and nums[i] <= pivot:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]

        nums[i], nums[low] = nums[low], nums[i]

        return i

    def quickSort(self, nums: [int], low: int, high: int) -> [int]:
        if low < high:
            pivot_i = self.randomPartition(nums, low, high)
            self.quickSort(nums, low, pivot_i - 1)
            self.quickSort(nums, pivot_i + 1, high)
        return nums


# nums = [3,2,3,1,2,4,5,5,6]
nums = [3, 2, 1, 5, 6, 4]
# Solution().findKthLargest(nums=nums, k=2)
Solution2().findKthLargest(nums=nums, k=2)
