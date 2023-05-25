#
# @lc app=leetcode.cn id=1377 lang=python3
#
# [1377] T 秒后青蛙的位置
#
# https://leetcode.cn/problems/frog-position-after-t-seconds/description/
#
# algorithms
# Hard (33.78%)
# Likes:    90
# Dislikes: 0
# Total Accepted:    13.9K
# Total Submissions: 34.1K
# Testcase Example:  '7\n[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]\n2\n4'
#
# 给你一棵由 n 个顶点组成的无向树，顶点编号从 1 到 n。青蛙从 顶点 1 开始起跳。规则如下：
#
#
# 在一秒内，青蛙从它所在的当前顶点跳到另一个 未访问 过的顶点（如果它们直接相连）。
# 青蛙无法跳回已经访问过的顶点。
# 如果青蛙可以跳到多个不同顶点，那么它跳到其中任意一个顶点上的机率都相同。
# 如果青蛙不能跳到任何未访问过的顶点上，那么它每次跳跃都会停留在原地。
#
#
# 无向树的边用数组 edges 描述，其中 edges[i] = [ai, bi] 意味着存在一条直接连通 ai 和 bi 两个顶点的边。
#
# 返回青蛙在 t 秒后位于目标顶点 target 上的概率。与实际答案相差不超过 10^-5 的结果将被视为正确答案。
#
#
#
# 示例 1：
#
#
#
#
# 输入：n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
# 输出：0.16666666666666666
# 解释：上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，第 1 秒 有 1/3 的概率跳到顶点 2 ，然后第 2 秒 有 1/2 的概率跳到顶点
# 4，因此青蛙在 2 秒后位于顶点 4 的概率是 1/3 * 1/2 = 1/6 = 0.16666666666666666 。
#
#
# 示例 2：
#
#
#
#
# 输入：n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
# 输出：0.3333333333333333
# 解释：上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，有 1/3 = 0.3333333333333333 的概率能够 1 秒 后跳到顶点 7
# 。
#
#
#
#
#
#
# 提示：
#
#
# 1 <= n <= 100
# edges.length == n - 1
# edges[i].length == 2
# 1 <= ai, bi <= n
# 1 <= t <= 50
# 1 <= target <= n
#
#
#

# @lc code=start
from typing import List


class Solution:
    def frogPosition(
        self, n: int, edges: List[List[int]], t: int, target: int
    ) -> float:
        graph = [[] for _ in range(n + 1)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        graph[1].append(0)

        ans = 0
        # print(graph)

        def dfs(node, p, t, res):
            # print(node, p, t, res, graph[node])
            nonlocal ans
            if node == target and (t == 0 or len(graph[node]) == 1):
                ans = 1 / res
                return True
            if node == target or t == 0:
                return False
            for child in graph[node]:
                if child != p:
                    # print(res, graph[node], "++++++")
                    if dfs(child, node, t - 1, res * (len(graph[node]) - 1)):
                        return True
            return False

        dfs(1, 0, t, 1)

        return ans


# @lc code=end
