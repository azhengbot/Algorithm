#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30204
#
# [53] 最大子数组和
#
# https://leetcode.cn/problems/maximum-subarray/description/
#
# algorithms
# Medium (55.71%)
# Likes:    6841
# Dislikes: 0
# Total Accepted:    1.9M
# Total Submissions: 3.4M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组 是数组中的一个连续部分。
#
#
#
# 示例 1：
#
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#
#
# 示例 2：
#
# 输入：nums = [1]
# 输出：1
#
#
# 示例 3：
#
# 输入：nums = [5,4,-1,7,8]
# 输出：23
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#
#
# 进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = [0] * n
        pre_sum[0] = nums[0]

        for i in range(1, n):
            pre_sum[i] = pre_sum[i - 1] + nums[i]

        pre_min = 0
        ans = -inf
        # print(pre_sum)
        for i in range(n):
            ans = max(ans, pre_sum[i] - pre_min)
            pre_min = min(pre_min, pre_sum[i])

        return ans


# @lc code=end


#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#

#
