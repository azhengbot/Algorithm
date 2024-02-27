#
# @lc app=leetcode.cn id=2867 lang=python3
#
# [2867] 统计树中的合法路径数目
#
# https://leetcode.cn/problems/count-valid-paths-in-a-tree/description/
#
# algorithms
# Hard (34.77%)
# Likes:    31
# Dislikes: 0
# Total Accepted:    4.9K
# Total Submissions: 11.1K
# Testcase Example:  '5\n[[1,2],[1,3],[2,4],[2,5]]'
#
# 给你一棵 n 个节点的无向树，节点编号为 1 到 n 。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i]
# = [ui, vi] 表示节点 ui 和 vi 在树中有一条边。
# 
# 请你返回树中的 合法路径数目 。
# 
# 如果在节点 a 到节点 b 之间 恰好有一个 节点的编号是质数，那么我们称路径 (a, b) 是 合法的 。
# 
# 注意：
# 
# 
# 路径 (a, b) 指的是一条从节点 a 开始到节点 b 结束的一个节点序列，序列中的节点 互不相同 ，且相邻节点之间在树上有一条边。
# 路径 (a, b) 和路径 (b, a) 视为 同一条 路径，且只计入答案 一次 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：n = 5, edges = [[1,2],[1,3],[2,4],[2,5]]
# 输出：4
# 解释：恰好有一个质数编号的节点路径有：
# - (1, 2) 因为路径 1 到 2 只包含一个质数 2 。
# - (1, 3) 因为路径 1 到 3 只包含一个质数 3 。
# - (1, 4) 因为路径 1 到 4 只包含一个质数 2 。
# - (2, 4) 因为路径 2 到 4 只包含一个质数 2 。
# 只有 4 条合法路径。
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：n = 6, edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]
# 输出：6
# 解释：恰好有一个质数编号的节点路径有：
# - (1, 2) 因为路径 1 到 2 只包含一个质数 2 。
# - (1, 3) 因为路径 1 到 3 只包含一个质数 3 。
# - (1, 4) 因为路径 1 到 4 只包含一个质数 2 。
# - (1, 6) 因为路径 1 到 6 只包含一个质数 3 。
# - (2, 4) 因为路径 2 到 4 只包含一个质数 2 。
# - (3, 6) 因为路径 3 到 6 只包含一个质数 3 。
# 只有 6 条合法路径。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 10^5
# edges.length == n - 1
# edges[i].length == 2
# 1 <= ui, vi <= n
# 输入保证 edges 形成一棵合法的树。
# 
# 
#

from math import isqrt

# @lc code=start
from typing import List

MX = 10 ** 5 + 1
is_prime = [True] * MX
is_prime[1] = False

for i in range(2, isqrt(MX) + 1):
    if is_prime[i]:
        for j in range(i*i, MX, i):
            is_prime[j] = False


class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n+1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(x, fa):
            nodes.append(x)
            for y in g[x]:
                if y != fa and not is_prime[y]:
                    dfs(y, x)

        ans = 0
        size = [0] * (n+1)

        for x in range(1, n+1):
            if not is_prime[x]:
                continue
            s = 0
            for y in g[x]:
                if is_prime[y]:
                    continue
                if size[y] == 0:
                    nodes = []
                    dfs(y, -1)
                    for z in nodes:
                        size[z] = len(nodes)
                
                ans += size[y] * s
                s += size[y]

            ans += s
        return ans

            

        
# @lc code=end

