# -*- coding: utf-8 -*-
"""
@Time ： 2024/6/11 下午8:50
@Auth ： simonzfei
@File ：0189.py
@IDE ：PyCharm
@Motto：thinking coding 
"""

"""
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]

示例 2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]

提示：

    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105

"""


class Solution(object):
    """"""

    # 轮转数组

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.

        根据列表循环移动规律，原列表（长度L）向右移动k次，nums[i]
        移动k次新的位置为(i + k) % L；即新列表向左反向移动计算新位置对应原始位置为(i + L - k) % L
        需要注意的是：python需要对原列表元素重新赋值才能重写
        31ms 击败48.37%
        """

        new_nums = []
        L = len(nums)
        print(L)

        for i in range(0, L):
            print('i', i)
            # new_pos = (i+k) % L# new position for transfer
            ori_position = (i + L - k) % L  # get the origin posion from new position
            print(ori_position)
            new_nums.append(nums[ori_position])
            print(new_nums)
        nums = new_nums
        print(nums)


nums = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate(nums=nums, k=3)
