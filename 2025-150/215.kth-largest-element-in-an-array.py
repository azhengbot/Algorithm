#
# @lc app=leetcode.cn id=215 lang=python3
# @lcpr version=30204
#
# [215] 数组中的第K个最大元素
#
# https://leetcode.cn/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (60.99%)
# Likes:    2596
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 2M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
#
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
#
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4], k = 2
# 输出: 5
#
#
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6], k = 4
# 输出: 4
#
#
#
# 提示：
#
#
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
            x = nums[0]
            l = [nu for nu in nums if nu > x]
            e = [nu for nu in nums if nu == x]
            h = [nu for nu in nums if nu < x]
            # print(l, e, h, k)
            if len(l) > k:
                return quick_select(l, k)
            elif len(l) + len(e) > k:
                return e[0]
            else:
                return quick_select(h, k - len(l) - len(e))

        return quick_select(nums, k - 1)


# s = Solution()
# s.findKthLargest([7, 1, 3, 5, 8, 9], 2)


# def partition(left, right):
#     # print(left, right)
#     # pivot_index = random.randint(left, right)
#     pivot_index = (left + right) // 2
#     pivot = nums[pivot_index]
#     nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
#     i = left
#     for j in range(left, right):
#         if nums[j] >= pivot:
#             nums[i], nums[j] = nums[j], nums[i]
#             i += 1

#     nums[i], nums[right] = nums[right], nums[i]
#     # print(i, nums[i], nums)

#     return i

# left, right = 0, len(nums) - 1

# while left <= right:
#     pivot_index = partition(left, right)
#     if pivot_index == k - 1:
#         return nums[pivot_index]
#     elif pivot_index < k - 1:
#         left = pivot_index + 1
#     else:
#         right = pivot_index - 1


# @lc code=end


#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#

#
