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
        ans = []
        m, n = len(matrix), len(matrix[0])
        path = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        used = [[False] * n for _ in range(m)]

        path_i = 0
        i, j = 0, 0

        for _ in range(m * n):
            ans.append(matrix[i][j])
            used[i][j] = True
            p = path[path_i]
            ni = i + p[0]
            nj = j + p[1]

            if ni >= m or nj >= n or ni < 0 or nj < 0 or used[ni][nj]:
                path_i = (path_i + 1) % 4
                ni = i - p[0]
                nj = j - p[1]
            i = i + path[path_i][0]
            j = j + path[path_i][1]

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

#
