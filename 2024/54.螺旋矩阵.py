#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode.cn/problems/spiral-matrix/description/
#
# algorithms
# Medium (50.02%)
# Likes:    1588
# Dislikes: 0
# Total Accepted:    451.8K
# Total Submissions: 901.2K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# -100 
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        tx = [0, 1, 0, -1]
        ty = [1, 0, -1, 0]
        used = [[0] * n for _ in range(m)]

        i, j = 0, 0
        t = 0
        total = m * n
        ans = [matrix[0][0]]
        used[0][0] = True

        for _ in range(total-1):
            i, j = i+tx[t], j+ty[t]
            if i < 0 or j < 0 or i >= m or j >= n or used[i][j]:
                i, j = i-tx[t], j-ty[t]
                t = (t + 1) % 4
                i, j = i+tx[t], j+ty[t]

            # print(i, j)
            used[i][j] = True
            ans.append(matrix[i][j])

        return ans

                    






# @lc code=end

