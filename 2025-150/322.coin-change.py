#
# @lc app=leetcode.cn id=322 lang=python3
# @lcpr version=30204
#
# [322] 零钱兑换
#
# https://leetcode.cn/problems/coin-change/description/
#
# algorithms
# Medium (49.62%)
# Likes:    2960
# Dislikes: 0
# Total Accepted:    972.2K
# Total Submissions: 1.9M
# Testcase Example:  '[1,2,5]\n11'
#
# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
#
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
#
# 你可以认为每种硬币的数量是无限的。
#
#
#
# 示例 1：
#
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
#
# 示例 2：
#
# 输入：coins = [2], amount = 3
# 输出：-1
#
# 示例 3：
#
# 输入：coins = [1], amount = 0
# 输出：0
#
#
#
#
# 提示：
#
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
#
#
#


# @lcpr-template-start

from functools import cache

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(i, amt):
            if i < 0:
                return 0 if amt == 0 else float("inf")
            if amt < 0:
                return float("inf")

            if amt == 0:
                return 0

            return min(dfs(i, amt - coins[i]) + 1, dfs(i - 1, amt))

        res = dfs(len(coins) - 1, amount)
        return res if res != float("inf") else -1


# @lc code=end


#
# @lcpr case=start
# [1, 2, 5]\n11\n
# @lcpr case=end

# @lcpr case=start
# [2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#
