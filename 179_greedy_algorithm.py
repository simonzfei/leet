"""

179. 最大数
中等
相关标签
相关企业

给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。



示例 1：

输入：nums = [10,2]
输出："210"

示例 2：

输入：nums = [3,30,34,5,9]
输出："9534330"



提示：

    1 <= nums.length <= 100
    0 <= nums[i] <= 109


"""
from typing import List
class Solution():
    """
    modify quick  sort
    """
    def largestNumber(self, nums: List[int])-> str:
        def quick_sort( l, r):
            if l >= r : return
            i, j = l , r
            while i < j:
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: j-=1
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: i+=1
                strs[i], strs[j] = strs[j], strs[i]
            strs[i] , strs[l] = strs[l], strs[i]
            quick_sort(l, i-1)
            quick_sort(i+1, r)


        strs = [str(num) for num in nums]
        quick_sort(0, len(nums)-1)
        if strs[-1] == "0": #be aware of the last one
            return "0"
        return ''.join(strs[::-1])

nums = [3,30,34,5,9]
print(Solution().largestNumber(nums=nums))