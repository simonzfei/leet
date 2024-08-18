

"""
34. 在排序数组中查找元素的第一个和最后一个位置
已解答
中等
相关标签
相关企业

给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。



示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：

输入：nums = [], target = 0
输出：[-1,-1]



提示：

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums 是一个非递减数组
    -109 <= target <= 109



"""


from  typing import  List




class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        first = -1
        last = -1
        while l <= r:
            middle = (l + r) // 2
            if nums[middle] == target:
                r = middle - 1  # key point 1
                first = middle
            elif nums[middle] > target:
                r = middle - 1
            elif nums[middle] < target:
                l = middle + 1

        l, r = 0, len(nums) - 1
        while l <= r:
            middle = (r + l) // 2
            if nums[middle] == target:
                last = middle
                l = middle + 1 # key point 2
            elif nums[middle] > target:
                r = middle - 1
            elif nums[middle] < target:
                l = middle + 1
        return [first, last]



