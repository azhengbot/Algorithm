#
# @lc app=leetcode.cn id=1267 lang=python3
#
# [1267] 统计参与通信的服务器
#
# https://leetcode.cn/problems/count-servers-that-communicate/description/
#
# algorithms
# Medium (61.96%)
# Likes:    89
# Dislikes: 0
# Total Accepted:    23.4K
# Total Submissions: 34.6K
# Testcase Example:  '[[1,0],[0,1]]'
#
# 这里有一幅服务器分布图，服务器的位置标识在 m * n 的整数矩阵网格 grid 中，1 表示单元格上有服务器，0 表示没有。
#
# 如果两台服务器位于同一行或者同一列，我们就认为它们之间可以进行通信。
#
# 请你统计并返回能够与至少一台其他服务器进行通信的服务器的数量。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[1,0],[0,1]]
# 输出：0
# 解释：没有一台服务器能与其他服务器进行通信。
#
# 示例 2：
#
#
#
# 输入：grid = [[1,0],[1,1]]
# 输出：3
# 解释：所有这些服务器都至少可以与一台别的服务器进行通信。
#
#
# 示例 3：
#
#
#
# 输入：grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# 输出：4
# 解释：第一行的两台服务器互相通信，第三列的两台服务器互相通信，但右下角的服务器无法与其他服务器通信。
#
#
#
#
# 提示：
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m <= 250
# 1 <= n <= 250
# grid[i][j] == 0 or 1
#
#
#

# @lc code=start
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        row = [0] * m
        col = [0] * n
        for i in range(m):
            row[i] = sum(grid[i])

        for j in range(n):
            col[j] = sum([row[j] for row in grid])

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row[i] > 1 or col[j] > 1):
                    cnt += 1

        return cnt


# @lc code=end
