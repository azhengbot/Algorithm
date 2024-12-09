# STUCK
# @lc app=leetcode.cn id=189 lang=python3
# @lcpr version=30204
#
# [189] 轮转数组
#
# https://leetcode.cn/problems/rotate-array/description/
#
# algorithms
# Medium (45.88%)
# Likes:    2276
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 2.3M
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
#
#
#
# 示例 1:
#
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]
#
#
# 示例 2:
#
# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释:
# 向右轮转 1 步: [99,-1,-100,3]
# 向右轮转 2 步: [3,99,-1,-100]
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5
#
#
#
#
# 进阶：
#
#
# 尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。
# 你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)

        k = k % n
        reverse(0, n - 1)
        # print(nums)
        reverse(0, k - 1)
        reverse(k, n - 1)


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [-1,-100,3,99]\n2\n
# @lcpr case=end

#

#
