#
# @lc app=leetcode.cn id=3098 lang=python3
#
# [3098] 求出所有子序列的能量和
#
# https://leetcode.cn/problems/find-the-sum-of-subsequence-powers/description/
#
# algorithms
# Hard (39.34%)
# Likes:    26
# Dislikes: 0
# Total Accepted:    5.6K
# Total Submissions: 10.5K
# Testcase Example:  '[1,2,3,4]\n3'
#
# 给你一个长度为 n 的整数数组 nums 和一个 正 整数 k 。
#
# 一个 子序列 的 能量 定义为子序列中 任意 两个元素的差值绝对值的 最小值 。
#
# 请你返回 nums 中长度 等于 k 的 所有 子序列的 能量和 。
#
# 由于答案可能会很大，将答案对 10^9 + 7 取余 后返回。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,3,4], k = 3
#
# 输出：4
#
# 解释：
#
# nums 中总共有 4 个长度为 3 的子序列：[1,2,3] ，[1,3,4] ，[1,2,4] 和 [2,3,4] 。能量和为 |2 - 3| +
# |3 - 4| + |2 - 1| + |3 - 4| = 4 。
#
#
# 示例 2：
#
#
# 输入：nums = [2,2], k = 2
#
# 输出：0
#
# 解释：
#
# nums 中唯一一个长度为 2 的子序列是 [2,2] 。能量和为 |2 - 2| = 0 。
#
#
# 示例 3：
#
#
# 输入：nums = [4,3,-1], k = 2
#
# 输出：10
#
# 解释：
#
# nums 总共有 3 个长度为 2 的子序列：[4,3] ，[4,-1] 和 [3,-1] 。能量和为 |4 - 3| + |4 - (-1)| + |3
# - (-1)| = 10 。
#
#
#
#
# 提示：
#
#
# 2 <= n == nums.length <= 50
# -10^8 <= nums[i] <= 10^8
# 2 <= k <= n
#
#
#

from functools import cache

# @lc code=start
from typing import List


class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        MOD = 10**9 + 7

        @cache
        def dfs(i, rest, ans, last):
            if rest == 0:
                return ans
            if n - i < rest:
                return 0

            r1 = dfs(i + 1, rest - 1, min(ans, nums[i] - last), nums[i])
            r2 = dfs(i + 1, rest, ans, last)

            return (r1 + r2) % MOD

        return dfs(0, k, float("inf"), float("-inf"))


# @lc code=end
