from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        opt = [[float("-inf"), float("-inf")] for i in range(n)]

        opt[0][0] = 0
        opt[0][1] = -prices[0]

        for i in range(1, n):
            opt[i][0] = max(opt[i - 1][0], opt[i - 1][1] + prices[i])

            opt[i][1] = max(opt[i - 1][0] - prices[i], opt[i - 1][1])

        # print(opt)
        return opt[n - 1][0]
