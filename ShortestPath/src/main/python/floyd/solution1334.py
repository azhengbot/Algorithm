from typing import List


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:

        matrix = [[float("inf") for i in range(n)] for i in range(n)]

        for i in range(n):
            matrix[i][i] = 0

        for edge in edges:
            x = edge[0]
            y = edge[1]
            z = edge[2]
            matrix[x][y] = matrix[y][x] = z

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

        min_neighbour = n
        ans = 0

        for i in range(n):
            neighbour = 0
            for j in range(n):
                if i != j and matrix[i][j] <= distanceThreshold:
                    neighbour += 1

            if neighbour < min_neighbour or neighbour == min_neighbour and i > ans:
                min_neighbour = neighbour
                ans = i

        return ans
