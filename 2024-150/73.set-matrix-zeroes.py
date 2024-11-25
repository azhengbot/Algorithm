#
# @lc app=leetcode.cn id=73 lang=python3
# @lcpr version=30204
#
# [73] 矩阵置零
#
# https://leetcode.cn/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (68.58%)
# Likes:    1131
# Dislikes: 0
# Total Accepted:    455.1K
# Total Submissions: 661.5K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
#
#
#
#
#
#
# 示例 1：
#
# 输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：[[1,0,1],[0,0,0],[1,0,1]]
#
#
# 示例 2：
#
# 输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# 输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1
#
#
#
#
# 进阶：
#
#
# 一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个仅使用常量空间的解决方案吗？
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        first_r = False
        first_c = False

        for c in range(m):
            if matrix[c][0] == 0:
                first_r = True

        for r in range(n):
            if matrix[0][r] == 0:
                first_c = True

        for c in range(1, m):
            for r in range(1, n):
                if matrix[c][r] == 0:
                    matrix[c][0] = 0
                    matrix[0][r] = 0
        # print(matrix, first_r, first_c)
        for c in range(m):
            for r in range(n):
                if c != 0 and r != 0 and (matrix[c][0] == 0 or matrix[0][r] == 0):
                    matrix[c][r] = 0

        if first_c:
            for r in range(n):
                matrix[0][r] = 0

        if first_r:
            for c in range(m):
                matrix[c][0] = 0


# @lc code=end


#
# @lcpr case=start
# [[1,1,1],[1,0,1],[1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,2,0],[3,4,5,2],[1,3,1,5]]\n
# @lcpr case=end

#

#
