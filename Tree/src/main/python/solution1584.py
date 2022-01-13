from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        self.fa = [i for i in range(n)]

        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dis = abs(points[i][0] - points[j][0]) + abs(
                    points[i][1] - points[j][1]
                )
                edges.append([i, j, dis])

        edges = sorted(edges, key=lambda x: x[2])

        ans = 0

        for edge in edges:
            x = edge[0]
            y = edge[1]
            z = edge[2]

            x = self.find(x)
            y = self.find(y)
            # if self.find(x) != self.find(y):   # 不能这么写，这么写，没办法合并，需要把x， y 重新赋值
            if x != y:
                ans += z
                self.fa[x] = y

        return ans

    def find(self, x):
        if x == self.fa[x]:
            return x

        self.fa[x] = self.find(self.fa[x])

        return self.fa[x]


s = Solution()

points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]

res = s.minCostConnectPoints(points)
print(res)
