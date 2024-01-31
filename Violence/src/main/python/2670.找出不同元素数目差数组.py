#
# @lc app=leetcode.cn id=2670 lang=python3
#
# [2670] 找出不同元素数目差数组
#
# https://leetcode.cn/problems/find-the-distinct-difference-array/description/
#
# algorithms
# Easy (76.53%)
# Likes:    27
# Dislikes: 0
# Total Accepted:    15.9K
# Total Submissions: 19.4K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给你一个下标从 0 开始的数组 nums ，数组长度为 n 。
# 
# nums 的 不同元素数目差 数组可以用一个长度为 n 的数组 diff 表示，其中 diff[i] 等于前缀 nums[0, ..., i]
# 中不同元素的数目 减去 后缀 nums[i + 1, ..., n - 1] 中不同元素的数目。
# 
# 返回 nums 的 不同元素数目差 数组。
# 
# 注意 nums[i, ..., j] 表示 nums 的一个从下标 i 开始到下标 j 结束的子数组（包含下标 i 和 j
# 对应元素）。特别需要说明的是，如果 i > j ，则 nums[i, ..., j] 表示一个空子数组。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3,4,5]
# 输出：[-3,-1,1,3,5]
# 解释：
# 对于 i = 0，前缀中有 1 个不同的元素，而在后缀中有 4 个不同的元素。因此，diff[0] = 1 - 4 = -3 。
# 对于 i = 1，前缀中有 2 个不同的元素，而在后缀中有 3 个不同的元素。因此，diff[1] = 2 - 3 = -1 。
# 对于 i = 2，前缀中有 3 个不同的元素，而在后缀中有 2 个不同的元素。因此，diff[2] = 3 - 2 = 1 。
# 对于 i = 3，前缀中有 4 个不同的元素，而在后缀中有 1 个不同的元素。因此，diff[3] = 4 - 1 = 3 。
# 对于 i = 4，前缀中有 5 个不同的元素，而在后缀中有 0 个不同的元素。因此，diff[4] = 5 - 0 = 5 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [3,2,3,4,2]
# 输出：[-2,-1,0,2,3]
# 解释：
# 对于 i = 0，前缀中有 1 个不同的元素，而在后缀中有 3 个不同的元素。因此，diff[0] = 1 - 3 = -2 。
# 对于 i = 1，前缀中有 2 个不同的元素，而在后缀中有 3 个不同的元素。因此，diff[1] = 2 - 3 = -1 。
# 对于 i = 2，前缀中有 2 个不同的元素，而在后缀中有 2 个不同的元素。因此，diff[2] = 2 - 2 = 0 。
# 对于 i = 3，前缀中有 3 个不同的元素，而在后缀中有 1 个不同的元素。因此，diff[3] = 3 - 1 = 2 。
# 对于 i = 4，前缀中有 3 个不同的元素，而在后缀中有 0 个不同的元素。因此，diff[4] = 3 - 0 = 3 。 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n == nums.length <= 50
# 1 <= nums[i] <= 50
# 
# 
#

from collections import Counter

# @lc code=start
from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = []

        for i in range(n):
            ans.append(len(set(nums[:i+1])) - len(set(nums[i+1:])))

        
        return ans


        

# @lc code=end

