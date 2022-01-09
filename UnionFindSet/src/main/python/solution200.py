from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        self.fa = [i for i in range(m * n)]

        dx = [1, 0, 0, -1]
        dy = [0, 1, -1, 0]

        for i in range(m):
            for j in range(n):
                for k in range(4):
                    if grid[i][j] == "0":
                        continue
                    ni = i + dx[k]
                    nj = j + dy[k]

                    if ni >= m or nj >= n or ni < 0 or nj < 0:
                        continue
                    if grid[ni][nj] == "0":
                        continue
                    # print(i*n + j, ni*n + nj)
                    self.union_set(i * n + j, ni * n + nj)

        ans = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans.add(self.find(i * n + j))
        # print(ans)
        # print(self.fa)
        return len(ans)

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
