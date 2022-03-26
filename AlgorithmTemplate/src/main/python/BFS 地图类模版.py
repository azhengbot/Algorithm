#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (56.71%)
# Likes:    1562
# Dislikes: 0
# Total Accepted:    403.9K
# Total Submissions: 709.8K
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
# 1
# grid[i][j] 的值为 '0' 或 '1'
#
#
#

# @lc code=start
from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        di = [1, 0, 0, -1]
        dj = [0, 1, -1, 0]

        used = [[False] * n for _ in range(m)]

        def bfs(i, j):
            dq = deque()
            dq.append([i, j])
            used[i][j] = True

            while len(dq) != 0:
                i, j = dq.popleft()
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]

                    if ni < 0 or ni >= m or nj < 0 or nj >= n:
                        continue
                    if grid[ni][nj] == "0" or used[ni][nj]:
                        continue

                    if grid[ni][nj] == "1":
                        dq.append([ni, nj])
                        used[ni][nj] = True

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                if used[i][j]:
                    continue

                bfs(i, j)
                ans += 1

        return ans


# @lc code=end
