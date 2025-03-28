# TODO
# @lc app=leetcode.cn id=45 lang=python3
# @lcpr version=30204
#
# [45] 跳跃游戏 II
#
# https://leetcode.cn/problems/jump-game-ii/description/
#
# algorithms
# Medium (44.47%)
# Likes:    2663
# Dislikes: 0
# Total Accepted:    836.1K
# Total Submissions: 1.9M
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
#
# 每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j]
# 处:
#
#
# 0 <= j <= nums[i]
# i + j < n
#
#
# 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
#
#
#
# 示例 1:
#
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#
#
# 示例 2:
#
# 输入: nums = [2,3,0,1,4]
# 输出: 2
#
#
#
#
# 提示:
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 1000
# 题目保证可以到达 nums[n-1]
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [inf] * n
        dp[0] = 0
        for i, nu in enumerate(nums):
            for j in range(i + 1, min(i + nu + 1, n)):
                dp[j] = min(dp[j], dp[i] + 1)
        print(dp)
        return dp[n - 1]


# @lc code=end


#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#

#
