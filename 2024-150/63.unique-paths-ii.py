#
# @lc app=leetcode.cn id=63 lang=python3
# @lcpr version=30204
#
# [63] 不同路径 II
#
# https://leetcode.cn/problems/unique-paths-ii/description/
#
# algorithms
# Medium (41.72%)
# Likes:    1315
# Dislikes: 0
# Total Accepted:    553.1K
# Total Submissions: 1.3M
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 给定一个 m x n 的整数数组 grid。一个机器人初始位于 左上角（即 grid[0][0]）。机器人尝试移动到 右下角（即 grid[m -
# 1][n - 1]）。机器人每次只能向下或者向右移动一步。
#
# 网格中的障碍物和空位置分别用 1 和 0 来表示。机器人的移动路径中不能包含 任何 有障碍物的方格。
#
# 返回机器人能够到达右下角的不同路径数量。
#
# 测试用例保证答案小于等于 2 * 10^9。
#
#
#
# 示例 1：
#
# 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：2
# 解释：3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
#
#
# 示例 2：
#
# 输入：obstacleGrid = [[0,1],[0,0]]
# 输出：1
#
#
#
#
# 提示：
#
#
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] 为 0 或 1
#
#
#


# @lcpr-template-start

from functools import lru_cache

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        to = ((0, 1), (1, 0))

        cnt = 0
        if obstacleGrid[-1][-1] == 1:
            return 0

        @lru_cache
        def dfs(i, j):
            nonlocal cnt
            ans = 0
            if i >= m or j >= n or i < 0 or j < 0:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if obstacleGrid[i][j] == 1:
                return 0
            for x, y in to:
                ans += dfs(i + x, j + y)

            return ans

        ans = dfs(0, 0)
        return ans


# @lc code=end


#
# @lcpr case=start
# [[0,0,0],[0,1,0],[0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[0,0]]\n
# @lcpr case=end

#