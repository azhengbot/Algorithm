from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        m = len(edges)
        self.fa = [i for i in range(m + 1)]

        for edge in edges:
            if self.find(edge[0]) == self.find(edge[1]):
                return edge

            else:
                self.union_set(edge[0], edge[1])

    def find(self, x):
        if x == self.fa[x]:
            return x

        self.fa[x] = self.find(self.fa[x])

        return self.fa[x]

    def union_set(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x != y:
            self.fa[x] = y
