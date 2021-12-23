# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n: int = len(prices)
        ans: int = 0
        for i in range(1, n):
            ans = max(prices[i] - prices[i - 1], 0) + ans

        return ans
