# -*- coding: utf-8 -*-
"""
@Time ： 2024/6/12 上午10:45
@Auth ： simonzfei
@File ：66.py
@IDE ：PyCharm
@Motto：thinking coding 
"""
"""
66. 加一
简单

给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例 2：

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：

输入：digits = [0]
输出：[1]
提示：

    1 <= digits.length <= 100
    0 <= digits[i] <= 9
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(0, len(digits))):
            if digits[i] + 1 <= 9:
                digits[i] += 1
                break
            elif i == 0:
                digits[i] = 0
                digits.insert(0, 1)
            else:
                digits[i] = 0
        return digits


# digits = [1,2,3]
digits = [9]
Solution().plusOne(digits=digits)
