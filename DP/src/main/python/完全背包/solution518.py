from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)  # N种物品

        opt = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]

        opt[0][0] = 1

        for i in range(1, n + 1):
            value = coins[i - 1]
            for j in range(amount + 1):
                opt[i][j] = opt[i - 1][j]

                k = 1
                while k * value <= j:
                    opt[i][j] = opt[i][j] + opt[i - 1][j - k * value]
                    k += 1

        return opt[n][amount]


s = Solution()

amount = 5
coins = [1, 2, 5]

res = s.change(amount, coins)
print(res)
