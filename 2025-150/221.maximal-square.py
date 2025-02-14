#
# @lc app=leetcode.cn id=221 lang=python3
# @lcpr version=30204
#
# [221] 最大正方形
#
# https://leetcode.cn/problems/maximal-square/description/
#
# algorithms
# Medium (50.91%)
# Likes:    1730
# Dislikes: 0
# Total Accepted:    360.8K
# Total Submissions: 708.4K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
#
#
#
# 示例 1：
#
# 输入：matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：4
#
#
# 示例 2：
#
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
#
#
# 示例 3：
#
# 输入：matrix = [["0"]]
# 输出：0
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] 为 '0' 或 '1'
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        max_side = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                    continue
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                max_side = max(max_side, dp[i][j])
        # print(dp)
        return max_side * max_side


# @lc code=end


#
# @lcpr case=start
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0","1"],["1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0"]]\n
# @lcpr case=end

#
