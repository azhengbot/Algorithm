# STUCK
# @lc app=leetcode.cn id=188 lang=python3
# @lcpr version=30204
#
# [188] 买卖股票的最佳时机 IV
#
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (51.48%)
# Likes:    1226
# Dislikes: 0
# Total Accepted:    295K
# Total Submissions: 572.4K
# Testcase Example:  '2\n[2,4,1]'
#
# 给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
#
#
# 示例 1：
#
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
#
# 示例 2：
#
# 输入：k = 2, prices = [3,2,6,5,0,3]
# 输出：7
# 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
# ⁠    随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3
# 。
#
#
#
# 提示：
#
#
# 1 <= k <= 100
# 1 <= prices.length <= 1000
# 0 <= prices[i] <= 1000
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-inf, -inf] for _ in range(k + 2)] for _ in range(n + 1)]

        for j in range(k + 2):
            dp[0][j][0] = 0
            # dp[0][j][1] = float(-inf)

        for i in range(1, n + 1):
            for j in range(1, k + 2):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][1] + prices[i - 1])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j][0] - prices[i - 1])
        print(dp)
        return dp[n][k + 1][0]


# @lc code=end


#
# @lcpr case=start
# 2\n[2,4,1]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[3,2,6,5,0,3]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[3,3,5,0,0,3,1,4]\n
# @lcpr case=end
#

#

# [
#     [[0, -inf], [0, -inf], [0, -inf]], 3
#     [[0, -3], [0, -3], [0, -3]], 3
#     [[0, -3], [0, -3], [0, -3]], 5
#     [[2, -3], [2, -3], [2, -3]], 0
#     [[2, 2], [2, 2], [2, 2]],    0
#     [[2, 2], [2, 2], [2, 2]],    3
#     [[5, 2], [5, 2], [5, 2]],    1
#     [[5, 4], [5, 4], [5, 4]],    4
#     [[8, 4], [8, 4], [8, 4]],
# ]
