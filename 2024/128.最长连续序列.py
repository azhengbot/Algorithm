#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# https://leetcode-cn.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (54.73%)
# Likes:    1228
# Dislikes: 0
# Total Accepted:    251.5K
# Total Submissions: 458.6K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# 
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 
# 示例 2：
# 
# 
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# -10^9 
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        ans = 1
        i, j = 0, 1
        n = len(nums)
        dup = 0
        # print(nums)
        while j < n:
            if nums[j] - nums[j-1] == 1:
                ans = max(j - i + 1 - dup, ans)
                j+=1
            elif nums[j] == nums[j-1]:
                j+=1
                dup += 1
            else:
                i = j
                j = i + 1
                dup = 0

        return ans
# @lc code=end

