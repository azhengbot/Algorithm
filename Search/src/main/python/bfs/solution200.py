from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [1, 0, 0, -1]
        dy = [0, 1, -1, 0]

        m = len(grid)
        n = len(grid[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        def bfs(i, j):
            queue = []
            queue.append((i, j))
            visited[i][j] = True
            while len(queue) != 0:
                # 出队
                i = queue[0][0]
                j = queue[0][1]
                queue.pop(0)
                for to in range(4):
                    ni = i + dx[to]
                    nj = j + dy[to]
                    if ni < 0 or nj < 0 or ni >= m or nj >= n:
                        continue
                    if visited[ni][nj]:
                        continue
                    if grid[ni][nj] == "0":
                        continue
                    queue.append((ni, nj))
                    visited[ni][nj] = True

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    ans += 1
                    bfs(i, j)

        return ans


s = Solution()
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]


res = s.numIslands(grid=grid)
print(res)
