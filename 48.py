# -*- coding: utf-8 -*-
"""
@Time ： 2024/6/21 上午10:48
@Auth ： simonzfei
@File ：48.py
@IDE ：PyCharm
@Motto：thinking coding 
"""


# class Solution(object):
#     def rotate(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: None Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix[0])
#         self.roate_one(matrix, n)
#
#     def roate_one(self, matrix, n):
#         if matrix == []:
#             return
#         elif n == 1:
#             return
#         elif n == 2:
#             matrix[0][0], matrix[0][1] = matrix[0][1], matrix[0][0]
#             matrix[0][0], matrix[1][0] = matrix[1][0], matrix[0][0]
#             matrix[1][0], matrix[1][1] = matrix[1][1], matrix[1][0]
#
#         else:
#             matrix[0][0], matrix[0][n - 1] = matrix[0][n - 1], matrix[0][0]
#             matrix[n - 1][0], matrix[0][0] = matrix[0][0], matrix[n - 1][0]
#             matrix[n - 1][n - 1], matrix[n - 1][0] = matrix[n - 1][0], matrix[n - 1][n - 1]
#             for i in range(1, n - 1):
#                 matrix[0][i], matrix[i][-i] = matrix[i][-i], matrix[0][i]
#                 matrix[-i][0], matrix[0][i] = matrix[0][i], matrix[-i][0]
#                 matrix[-1][-i], matrix[-i][0] = matrix[-i][0], matrix[-1][-i]
#
#         self.roate_one(matrix[1:-1][1:-1], n - 1)
#
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(matrix)
# print(Solution().rotate(matrix))

"""
按层次进行旋转，每次处理矩阵的外层。
对每一层进行4个角的交换。
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        self.rotate_layer(matrix, 0, n)

    def rotate_layer(self, matrix, layer, n):
        if n <= 1:
            return

        # Process the current layer
        for i in range(layer, layer + n - 1):
            top = matrix[layer][i]
            right = matrix[i][layer + n - 1]
            bottom = matrix[layer + n - 1][layer + n - 1 - (i - layer)]
            left = matrix[layer + n - 1 - (i - layer)][layer]

            matrix[layer][i] = left
            matrix[i][layer + n - 1] = top
            matrix[layer + n - 1][layer + n - 1 - (i - layer)] = right
            matrix[layer + n - 1 - (i - layer)][layer] = bottom

        # Recur for inner layers
        self.rotate_layer(matrix, layer + 1, n - 2)

# 示例 1
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Before rotation:", matrix1)
Solution().rotate(matrix1)
print("After rotation:", matrix1)  # 输出: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

# 示例 2
matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
print("Before rotation:", matrix2)
Solution().rotate(matrix2)
print("After rotation:", matrix2)  # 输出: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

