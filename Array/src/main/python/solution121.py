from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        pre_min = [0 for _ in range(n)]

        pre_min[0] = prices[0]
        for i in range(1, n):
            pre_min[i] = min(pre_min[i - 1], prices[i])

        ans = 0

        for i in range(1, n):
            ans = max(prices[i] - pre_min[i - 1], ans)

        return ans
