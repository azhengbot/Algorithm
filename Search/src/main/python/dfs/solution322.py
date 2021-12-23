from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        ans = 0
        count = 0
        all_count = []

        def dfs(coin):
            nonlocal ans, count
            if ans > amount:
                return
            if ans == amount:
                all_count.append(count)
                return

            ans += coin
            count += 1
            for i in coins:
                dfs(i)
                ans -= coin
                count -= 1

        for coin in coins:
            dfs(coin)

        return min(all_count)


s = Solution()
coins = [1, 2, 5]
amount = 11

res = s.coinChange(coins, amount)
print(res)
