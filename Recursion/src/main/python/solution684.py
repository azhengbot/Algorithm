# 找环
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 1
        self.has_cycle = False
        for edge in edges:
            x = edge[0]
            y = edge[1]

            n = max(n, max(x, y))

        to = [[] for i in range(n + 1)]
        visited = [False for i in range(n + 1)]

        def dfs(x, father):
            visited[x] = True

            for y in to[x]:
                if y == father:
                    continue
                if not visited[y]:
                    dfs(y, x)
                else:
                    self.has_cycle = True

            visited[x] = False

        for edge in edges:
            x = edge[0]
            y = edge[1]

            to[x].append(y)
            to[y].append(x)

            # self.has_cycle = False

            dfs(x, 0)

            if self.has_cycle:
                return edge


s = Solution()
edges = [[1, 2], [1, 3], [2, 3]]
res = s.findRedundantConnection(edges=edges)
print(res)