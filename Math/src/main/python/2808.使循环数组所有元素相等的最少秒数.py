#
# @lc app=leetcode.cn id=2808 lang=python3
#
# [2808] 使循环数组所有元素相等的最少秒数
#
# https://leetcode.cn/problems/minimum-seconds-to-equalize-a-circular-array/description/
#
# algorithms
# Medium (36.29%)
# Likes:    50
# Dislikes: 0
# Total Accepted:    9.2K
# Total Submissions: 18.1K
# Testcase Example:  '[1,2,1,2]'
#
# 给你一个下标从 0 开始长度为 n 的数组 nums 。
# 
# 每一秒，你可以对数组执行以下操作：
# 
# 
# 对于范围在 [0, n - 1] 内的每一个下标 i ，将 nums[i] 替换成 nums[i] ，nums[(i - 1 + n) % n] 或者
# nums[(i + 1) % n] 三者之一。
# 
# 
# 注意，所有元素会被同时替换。
# 
# 请你返回将数组 nums 中所有元素变成相等元素所需要的 最少 秒数。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,2,1,2]
# 输出：1
# 解释：我们可以在 1 秒内将数组变成相等元素：
# - 第 1 秒，将每个位置的元素分别变为 [nums[3],nums[1],nums[3],nums[3]] 。变化后，nums = [2,2,2,2]
# 。
# 1 秒是将数组变成相等元素所需要的最少秒数。
# 
# 
# 示例 2：
# 
# 输入：nums = [2,1,3,3,2]
# 输出：2
# 解释：我们可以在 2 秒内将数组变成相等元素：
# - 第 1 秒，将每个位置的元素分别变为 [nums[0],nums[2],nums[2],nums[2],nums[3]] 。变化后，nums =
# [2,3,3,3,3] 。
# - 第 2 秒，将每个位置的元素分别变为 [nums[1],nums[1],nums[2],nums[3],nums[4]] 。变化后，nums =
# [3,3,3,3,3] 。
# 2 秒是将数组变成相等元素所需要的最少秒数。
# 
# 
# 示例 3：
# 
# 输入：nums = [5,5,5,5]
# 输出：0
# 解释：不需要执行任何操作，因为一开始数组中的元素已经全部相等。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n == nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 
# 
#

from collections import defaultdict

# @lc code=start
from typing import List


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        idx_map = defaultdict(list)
        n = len(nums)

        ans = n
        for idx, nu in enumerate(nums):
            idx_map[nu].append(idx)

        for k, v_lst in idx_map.items():
            max_sub_ans = 0
            m = len(v_lst)
            for j in range(m):
                if j == 0:
                    max_sub_ans = max(max_sub_ans, n - v_lst[-1] + v_lst[0] -1)
                    continue
                max_sub_ans = max(max_sub_ans, v_lst[j] - v_lst[j-1] - 1)
            print(k, max_sub_ans)
            ans = min(ans, max_sub_ans)
           
        return ans//2 + 1 if ans % 2 else ans//2
            
            

# @lc code=end

