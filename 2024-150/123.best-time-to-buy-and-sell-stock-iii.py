# STUCK
# @lc app=leetcode.cn id=123 lang=python3
# @lcpr version=30204
#
# [123] 买卖股票的最佳时机 III
#
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (61.39%)
# Likes:    1769
# Dislikes: 0
# Total Accepted:    377.6K
# Total Submissions: 614.6K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
#
#
# 示例 1:
#
# 输入：prices = [3,3,5,0,0,3,1,4]
# 输出：6
# 解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
# 随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
#
# 示例 2：
#
# 输入：prices = [1,2,3,4,5]
# 输出：4
# 解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4
# 。
# 注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
# 因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#
#
# 示例 3：
#
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这个情况下, 没有交易完成, 所以最大利润为 0。
#
# 示例 4：
#
# 输入：prices = [1]
# 输出：0
#
#
#
#
# 提示：
#
#
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^5
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = 2
        n = len(prices)
        dp = [[[-inf, -inf] for _ in range(k + 2)] for _ in range(n + 1)]
        # print(dp)
        for j in range(1, k + 2):
            dp[0][j][0] = 0

        for i in range(n):
            for j in range(1, k + 2):
                dp[i + 1][j][0] = max(dp[i][j][0], dp[i][j - 1][1] + prices[i])
                dp[i + 1][j][1] = max(dp[i][j][1], dp[i][j][0] - prices[i])

        # print(dp)
        return dp[n][k + 1][0]


# @lc code=end


#
# @lcpr case=start
# [3,3,5,0,0,3,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#