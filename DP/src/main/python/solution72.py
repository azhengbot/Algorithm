class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = " " + word1
        word2 = " " + word2
        m, n = len(word1), len(word2)

        opt = [[float("inf") for _ in range(n)] for _ in range(m)]

        for i in range(m):
            opt[i][0] = i

        for j in range(n):
            opt[0][j] = j

        for i in range(1, m):
            for j in range(1, n):
                if word1[i] == word2[j]:
                    opt[i][j] = min(
                        opt[i - 1][j] + 1, opt[i][j - 1] + 1, opt[i - 1][j - 1]
                    )
                else:
                    opt[i][j] = min(
                        opt[i - 1][j] + 1, opt[i][j - 1] + 1, opt[i - 1][j - 1] + 1
                    )

        # print(opt)
        return opt[m - 1][n - 1]
