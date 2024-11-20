#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30204
#
# [54] 螺旋矩阵
#
# https://leetcode.cn/problems/spiral-matrix/description/
#
# algorithms
# Medium (52.07%)
# Likes:    1793
# Dislikes: 0
# Total Accepted:    625.1K
# Total Submissions: 1.2M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
#
#
#
# 示例 1：
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
#
# 示例 2：
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
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        used = [[0] * n for _ in range(m)]
        to_x = [0, 1, 0, -1]
        to_y = [1, 0, -1, 0]
        k = 0
        ans = []

        total = m * n

        for _ in range(total):
            ans.append(matrix[i][j])
            used[i][j] = 1
            ni, nj = i + to_x[k], j + to_y[k]

            if ni >= m or nj >= n or ni < 0 or nj < 0 or used[ni][nj]:
                k = (k + 1) % 4
                ni, nj = i + to_x[k], j + to_y[k]

            i, j = ni, nj

        return ans


# @lc code=end


#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#
