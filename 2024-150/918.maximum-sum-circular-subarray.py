# STUCK
# @lc app=leetcode.cn id=918 lang=python3
# @lcpr version=30204
#
# [918] 环形子数组的最大和
#
# https://leetcode.cn/problems/maximum-sum-circular-subarray/description/
#
# algorithms
# Medium (43.50%)
# Likes:    768
# Dislikes: 0
# Total Accepted:    104K
# Total Submissions: 238.2K
# Testcase Example:  '[1,-2,3,-2]'
#
# 给定一个长度为 n 的环形整数数组 nums ，返回 nums 的非空 子数组 的最大可能和 。
#
# 环形数组 意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i]
# 的前一个元素是 nums[(i - 1 + n) % n] 。
#
# 子数组 最多只能包含固定缓冲区 nums 中的每个元素一次。形式上，对于子数组 nums[i], nums[i + 1], ..., nums[j]
# ，不存在 i <= k1, k2 <= j 其中 k1 % n == k2 % n 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,-2,3,-2]
# 输出：3
# 解释：从子数组 [3] 得到最大和 3
#
#
# 示例 2：
#
# 输入：nums = [5,-3,5]
# 输出：10
# 解释：从子数组 [5,5] 得到最大和 5 + 5 = 10
#
#
# 示例 3：
#
# 输入：nums = [3,-2,2,-3]
# 输出：3
# 解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3
#
#
#
#
# 提示：
#
#
# n == nums.length
# 1 <= n <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4​​​​​​​
#
#
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int: ...


# @lc code=end


#
# @lcpr case=start
# [1,-2,3,-2]\n
# @lcpr case=end

# @lcpr case=start
# [5,-3,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,-2,2,-3]\n
# @lcpr case=end

# @lcpr case=start
# [-3,-2,-3]\n
# @lcpr case=end

# @lcpr case=start
# [3,-1,2,-1]\n
# @lcpr case=end
#

#
#
