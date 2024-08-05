# -*- coding: utf-8 -*-
"""
@Time ： 2024/6/12 下午3:22
@Auth ： simonzfei
@File ：54.py
@IDE ：PyCharm
@Motto：thinking coding 
"""
"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
示例 1：

输入：matrix = 
            [[1,2,3],
             [4,5,6],
             [7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：

输入：matrix = [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

提示：

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]

        执行用时分布
        16ms
        击败45.82%
        复杂度分析
        消耗内存分布
        11.47MB
        击败28.68%
        """
        out_list = []
        while matrix:
            if  len(matrix) ==1: # 处理只有一行的情况
                print(matrix)
                out_list.extend(matrix[0])
                return out_list
            elif len(matrix[0])== 1: # 处理只有一列的情况
                print(matrix)
                out_list.extend([row[0] for row in matrix])
                return out_list
            # 添加顶部一行
            out_list.extend(matrix.pop(0))

            # 添加右边一列
            if matrix and matrix[0]:
                for row in matrix:
                    out_list.append(row.pop())

            # 添加底部一行，逆序
            if matrix:
                out_list.extend(matrix.pop(-1)[::-1])

            # 添加左边一列，逆序
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    out_list.append(row.pop(0))
        return out_list



# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[91,100,111,112]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
ll = matrix.pop()
print(Solution().spiralOrder(matrix = matrix))

"""
https://assets.leetcode-cn.com/solution-static/54/54_fig1.png
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()
        
        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order

"""