#
# @lc app=leetcode.cn id=31 lang=python3
# @lcpr version=30204
#
# [31] 下一个排列
#
# https://leetcode.cn/problems/next-permutation/description/
#
# algorithms
# Medium (40.52%)
# Likes:    2650
# Dislikes: 0
# Total Accepted:    603.5K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3]'
#
# 整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
#
#
# 例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
#
#
# 整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列
# 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
#
#
# 例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
# 类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
# 而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
#
#
# 给你一个整数数组 nums ，找出 nums 的下一个排列。
#
# 必须 原地 修改，只允许使用额外常数空间。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[1,3,2]
#
#
# 示例 2：
#
# 输入：nums = [3,2,1]
# 输出：[1,2,3]
#
#
# 示例 3：
#
# 输入：nums = [1,1,5]
# 输出：[1,5,1]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i == -1:
            nums.reverse()

        j = n - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]
        # print(i, j)

        nums[i + 1 :] = sorted(nums[i + 1 :])


# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,5]\n
# @lcpr case=end

#

#
