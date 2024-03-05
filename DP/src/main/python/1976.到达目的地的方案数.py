#
# @lc app=leetcode.cn id=1976 lang=python3
#
# [1976] 到达目的地的方案数
#
# https://leetcode.cn/problems/number-of-ways-to-arrive-at-destination/description/
#
# algorithms
# Medium (37.16%)
# Likes:    118
# Dislikes: 0
# Total Accepted:    15.7K
# Total Submissions: 35.5K
# Testcase Example:  '7\n[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]'
#
# 你在一个城市里，城市由 n 个路口组成，路口编号为 0 到 n - 1 ，某些路口之间有 双向
# 道路。输入保证你可以从任意路口出发到达其他任意路口，且任意两个路口之间最多有一条路。
# 
# 给你一个整数 n 和二维整数数组 roads ，其中 roads[i] = [ui, vi, timei] 表示在路口 ui 和 vi 之间有一条需要花费
# timei 时间才能通过的道路。你想知道花费 最少时间 从路口 0 出发到达路口 n - 1 的方案数。
# 
# 请返回花费 最少时间 到达目的地的 路径数目 。由于答案可能很大，将结果对 10^9 + 7 取余 后返回。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 7, roads =
# [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
# 输出：4
# 解释：从路口 0 出发到路口 6 花费的最少时间是 7 分钟。
# 四条花费 7 分钟的路径分别为：
# - 0 ➝ 6
# - 0 ➝ 4 ➝ 6
# - 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
# - 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6
# 
# 
# 示例 2：
# 
# 输入：n = 2, roads = [[1,0,10]]
# 输出：1
# 解释：只有一条从路口 0 到路口 1 的路，花费 10 分钟。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 200
# n - 1 <= roads.length <= n * (n - 1) / 2
# roads[i].length == 3
# 0 <= ui, vi <= n - 1
# 1 <= timei <= 10^9
# ui != vi
# 任意两个路口之间至多有一条路。
# 从任意路口出发，你能够到达其他任意路口。
# 
# 
#

from collections import defaultdict

# @lc code=start
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        g = [[float("inf") for _ in range(n)] for _ in range(n)]

        for x, y, z in roads:
            g[x][y] = z
            g[y][x] = z
        
        done = [False] * n
        dis = [inf] * n
        f = [0] * n

        dis[0] = 0
        f[0] = 1


        while 1:
            x = -1

            for i, ok in enumerate(done):
                if not ok and (x < 0 or dis[i] < dis[x]):
                    x = i
            if x == n - 1:
                return f[n-1]

            done[x] = True
            dx = dis[x]    

            for y, d in enumerate(g[x]):
                new_dis = dx + d
                if new_dis < dis[y]:
                    dis[y] = new_dis
                    f[y] = f[x]
                elif new_dis == dis[y]:
                    f[y] = (f[y] + f[x]) % MOD
            
        

            
            

# @lc code=end

