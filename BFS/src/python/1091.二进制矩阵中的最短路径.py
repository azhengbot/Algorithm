#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#
# https://leetcode.cn/problems/shortest-path-in-binary-matrix/description/
#
# algorithms
# Medium (38.73%)
# Likes:    288
# Dislikes: 0
# Total Accepted:    66.7K
# Total Submissions: 169.3K
# Testcase Example:  '[[0,1],[1,0]]'
#
# 给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。
#
# 二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n -
# 1)）的路径，该路径同时满足下述要求：
#
#
# 路径途经的所有单元格都的值都是 0 。
# 路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
#
#
# 畅通路径的长度 是该路径途经的单元格总数。
#
#
#
# 示例 1：
#
#
# 输入：grid = [[0,1],[1,0]]
# 输出：2
#
#
# 示例 2：
#
#
# 输入：grid = [[0,0,0],[1,1,0],[1,1,0]]
# 输出：4
#
#
# 示例 3：
#
#
# 输入：grid = [[1,0,0],[1,1,0],[1,1,0]]
# 输出：-1
#
#
#
#
# 提示：
#
#
# n == grid.length
# n == grid[i].length
# 1
# grid[i][j] 为 0 或 1
#
#
#

from collections import deque

# @lc code=start
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        x = [0, 1, -1, 0, 1, -1, 1, -1]
        y = [-1, 0, 0, 1, 1, -1, -1, 1]

        n = len(grid)
        used = [[0] * n for _ in range(n)]
        dq = deque()
        dq.append((0, 0))
        used[0][0] = True
        cnt = 1
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        while dq:
            # print(dq, cnt)
            m = len(dq)
            for _ in range(m):
                i, j = dq.popleft()
                if i == n - 1 and j == n - 1:
                    return cnt
                for t in range(8):
                    ni, nj = i + x[t], j + y[t]
                    if ni < 0 or nj < 0 or ni >= n or nj >= n or grid[ni][nj] == 1:
                        continue
                    if used[ni][nj]:
                        continue
                    dq.append((ni, nj))
                    used[ni][nj] = True
            cnt += 1

        return -1


# @lc code=end

s = Solution()
grid = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0],
]  # 4

grid = [
    [1, 0, 0],
    [1, 1, 0],
    [1, 1, 0],
]  # 4

res = s.shortestPathBinaryMatrix(grid)
print(res)
