#
# @lc app=leetcode.cn id=1155 lang=python3
#
# [1155] 掷骰子等于目标和的方法数
#
# https://leetcode.cn/problems/number-of-dice-rolls-with-target-sum/description/
#
# algorithms
# Medium (51.50%)
# Likes:    206
# Dislikes: 0
# Total Accepted:    25K
# Total Submissions: 45.1K
# Testcase Example:  '1\n6\n3'
#
# 这里有 n 个一样的骰子，每个骰子上都有 k 个面，分别标号为 1 到 k 。
#
# 给定三个整数 n ,  k 和 target ，返回可能的方式(从总共 k^n 种方式中)滚动骰子的数量，使正面朝上的数字之和等于 target 。
#
# 答案可能很大，你需要对 10^9 + 7 取模 。
#
#
#
# 示例 1：
#
#
# 输入：n = 1, k = 6, target = 3
# 输出：1
# 解释：你扔一个有 6 个面的骰子。
# 得到 3 的和只有一种方法。
#
#
# 示例 2：
#
#
# 输入：n = 2, k = 6, target = 7
# 输出：6
# 解释：你扔两个骰子，每个骰子有 6 个面。
# 得到 7 的和有 6 种方法：1+6 2+5 3+4 4+3 5+2 6+1。
#
#
# 示例 3：
#
#
# 输入：n = 30, k = 30, target = 500
# 输出：222616187
# 解释：返回的结果必须是对 10^9 + 7 取模。
#
#
#
# 提示：
#
#
# 1 <= n, k <= 30
# 1 <= target <= 1000
#
#
#


# @lc code=start
from functools import cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        @cache
        def dfs(x, t):
            ans = 0
            if t <= 0:
                return 0
            if x == 1:
                if t <= k:
                    return 1
                return 0
            for i in range(1, k + 1):
                ans += dfs(x - 1, t - i) % MOD

            return ans

        return dfs(n, target) % MOD


# @lc code=end
