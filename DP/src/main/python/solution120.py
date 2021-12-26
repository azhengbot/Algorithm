from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        opt = [[0 for i in range(n)] for i in range(n)]

        opt[0][0] = triangle[0][0]

        for i in range(1, n):
            for j in range(len(triangle[i])):
                if j - 1 < 0:
                    opt[i][j] = triangle[i][j] + opt[i - 1][j]
                elif j >= len(triangle[i - 1]):
                    opt[i][j] = triangle[i][j] + opt[i - 1][j - 1]
                else:
                    opt[i][j] = triangle[i][j] + min(opt[i - 1][j], opt[i - 1][j - 1])

        return min(opt[n - 1])
