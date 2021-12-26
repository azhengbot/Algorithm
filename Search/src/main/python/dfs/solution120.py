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

        print(opt)
        return min(opt[n - 1])

        """
        dfs 搜索
        会超时
        """
        # ans_list = []

        # def dfs(m, n, ans):
        #     if m + 1 >= len(triangle):
        #         ans_list.append(ans)
        #         return

        #     ans1 = ans + triangle[m + 1][n]
        #     dfs(m + 1, n, ans1)

        #     ans2 = ans + triangle[m + 1][n + 1]
        #     dfs(m + 1, n + 1, ans2)

        # dfs(0, 0, triangle[0][0])
        # print(ans_list)
        # return min(ans_list)


s = Solution()

# triangle = [[2], [3, 4]]
triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
res = s.minimumTotal(triangle)
print(res)
