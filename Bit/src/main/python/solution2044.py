#
# @lc app=leetcode.cn id=2044 lang=python3
#
# [2044] 统计按位或能得到最大值的子集数目
#
# https://leetcode-cn.com/problems/count-number-of-maximum-bitwise-or-subsets/description/
#
# algorithms
# Medium (74.54%)
# Likes:    75
# Dislikes: 0
# Total Accepted:    19.7K
# Total Submissions: 24K
# Testcase Example:  '[3,1]'
#
# 给你一个整数数组 nums ，请你找出 nums 子集 按位或 可能得到的 最大值 ，并返回按位或能得到最大值的 不同非空子集的数目 。
#
# 如果数组 a 可以由数组 b 删除一些元素（或不删除）得到，则认为数组 a 是数组 b 的一个 子集 。如果选中的元素下标位置不一样，则认为两个子集 不同
# 。
#
# 对数组 a 执行 按位或 ，结果等于 a[0] OR a[1] OR ... OR a[a.length - 1]（下标从 0 开始）。
#
#
#
# 示例 1：
#
#
# 输入：nums = [3,1]
# 输出：2
# 解释：子集按位或能得到的最大值是 3 。有 2 个子集按位或可以得到 3 ：
# - [3]
# - [3,1]
#
#
# 示例 2：
#
#
# 输入：nums = [2,2,2]
# 输出：7
# 解释：[2,2,2] 的所有非空子集的按位或都可以得到 2 。总共有 2^3 - 1 = 7 个子集。
#
#
# 示例 3：
#
#
# 输入：nums = [3,2,1,5]
# 输出：6
# 解释：子集按位或可能的最大值是 7 。有 6 个子集按位或可以得到 7 ：
# - [3,5]
# - [3,1,5]
# - [3,2,5]
# - [3,2,1,5]
# - [2,5]
# - [2,1,5]
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 16
# 1 <= nums[i] <= 10^5
#
#
#

# @lc code=start
from typing import List


class Solution:
    # def countMaxOrSubsets(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     mask = 1 << n

    #     max_val = 0
    #     cnt = 0

    #     for s in range(mask):
    #         val = 0
    #         for i in range(n):
    #             if (s >> i) & 1 == 1:
    #                 val |= nums[i]
    #         if val > max_val:
    #             max_val = val
    #             cnt = 1
    #         elif val == max_val:
    #             cnt += 1

    #     return cnt

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dic = {}

        for i in range(20):
            # 获取 lowbit， 从右往左第一个为 1 的位置
            dic[1 << i] = i
            # map[bin(1 << i)[2:]] = i

        print(dic)

        n = len(nums)
        mask = 1 << n

        dp = [0 for _ in range(mask)]

        max_val = 0
        cnt = 0

        for s in range(1, mask):
            # "11000" & "-11000" = "1000"
            lowbit = s & -s
            idx = dic[lowbit]

            prev = s - lowbit

            dp[s] = dp[prev] | nums[idx]

            if dp[s] > max_val:
                max_val = dp[s]
                cnt = 1
            elif dp[s] == max_val:
                cnt += 1

        return cnt


s = Solution()
res = s.countMaxOrSubsets([3, 2, 1, 5])
print(res)

# @lc code=end
