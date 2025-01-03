# STUCK
# @lc app=leetcode.cn id=64 lang=python3
# @lcpr version=30204
#
# [64] 最小路径和
#
# https://leetcode.cn/problems/minimum-path-sum/description/
#
# algorithms
# Medium (71.18%)
# Likes:    1744
# Dislikes: 0
# Total Accepted:    685K
# Total Submissions: 961.2K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
#
#
# 示例 1：
#
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
#
#
# 示例 2：
#
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
#
#
#
#
# 提示：
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200
#
#
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[float(inf)] * n for _ in range(m)]

        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                if i - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + grid[i][j])
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + grid[i][j])

        return dp[m - 1][n - 1]


# @lc code=end


#
# @lcpr case=start
# [[1,3,1],[1,5,1],[4,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6]]\n
# @lcpr case=end

#
