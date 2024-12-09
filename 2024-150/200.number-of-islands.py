#
# @lc app=leetcode.cn id=200 lang=python3
# @lcpr version=30204
#
# [200] 岛屿数量
#
# https://leetcode.cn/problems/number-of-islands/description/
#
# algorithms
# Medium (61.67%)
# Likes:    2646
# Dislikes: 0
# Total Accepted:    960.9K
# Total Submissions: 1.6M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
#
#
# 示例 1：
#
# 输入：grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# 输出：1
#
#
# 示例 2：
#
# 输入：grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# 输出：3
#
#
#
#
# 提示：
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] 的值为 '0' 或 '1'
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        used = [[False] * n for _ in range(m)]
        to = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(i, j):
            used[i][j] = True
            for x, y in to:
                ni = i + x
                nj = j + y
                # print((i, j), (x, y), (ni, nj))
                if (
                    ni < 0
                    or nj < 0
                    or ni >= m
                    or nj >= n
                    or grid[ni][nj] == "0"
                    or used[ni][nj]
                ):
                    continue
                dfs(ni, nj)

        ans = 0
        for i in range(m):
            for j in range(n):
                if used[i][j] or grid[i][j] == "0":
                    continue
                dfs(i, j)
                # print(used)
                ans += 1

        return ans


# @lc code=end


#
# @lcpr case=start
# [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
# @lcpr case=end

#

#
