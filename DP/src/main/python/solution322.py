# https://leetcode-cn.com/problems/coin-change/
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        ans = float("INF")

        opt = [ans for _ in range(amount + 1)]
        opt[0] = 0

        for i in range(1, amount + 1):

            for coin in coins:

                if i - coin < 0:
                    continue

                opt[i] = min(opt[i], opt[i - coin] + 1)

        return opt[amount] if opt[amount] != float("INF") else -1
