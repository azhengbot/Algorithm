#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode.cn/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (46.42%)
# Likes:    2034
# Dislikes: 0
# Total Accepted:    681.3K
# Total Submissions: 1.5M
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 target 。
# 
# 找出该数组中满足其总和大于等于 target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr]
# ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
# 
# 
# 示例 2：
# 
# 
# 输入：target = 4, nums = [1,4,4]
# 输出：1
# 
# 
# 示例 3：
# 
# 
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# 
# 
# 
# 
# 进阶：
# 
# 
# 如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        # pre_sum = [0] * (n+1)
        # for i in range(1, n+1):
        #     pre_sum[i] = nums[i-1] + pre_sum[i-1]
        if max(nums) >= target:
            return 1
        if sum(nums) < target:
            return 0
        ans = n
        start, end = 0, 0
        su = 0
        while end < n:
            su += nums[end]
            if su < target:
                end += 1
            else:
                # print(ans, start, end, su)
                while su >= target and start < end:
                    ans = min(ans, end - start + 1)
                    su -= nums[start]
                    start += 1
                    # print(su, start, end)
                end += 1
                
        return ans
                

        
# @lc code=end

