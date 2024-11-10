# TODO
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30204
#
# [15] 三数之和
#
# https://leetcode.cn/problems/3sum/description/
#
# algorithms
# Medium (38.61%)
# Likes:    7132
# Dislikes: 0
# Total Accepted:    2M
# Total Submissions: 5.3M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j !=
# k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
# 
# 
# 示例 2：
# 
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
# 
# 
# 示例 3：
# 
# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        ans = []
        for i, nu in enumerate(nums):
            if i > 0 and nu == nums[i-1]:
                continue
            k, j = i + 1, n-1 
            while k < j:
                if nu + nums[k] + nums[j] < 0:
                    k += 1
                elif nu + nums[k] + nums[j] > 0:
                    j -= 1
                else:
                    ans.append((nu, nums[k], nums[j]))
                    k += 1
                    j -= 1
        ans = set(ans)
        ans = [list(x) for x in ans]
        return ans
        
        
            
                









    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     n = len(nums)
    #     ans = []
    #     nums.sort()
    #     for i in range(n):
    #         if i > 0 and nums[i] == nums[i-1]:
    #             continue
    #         if nums[i] > 0:
    #             break
    #         for j in range(i+1, n):
    #             if j > i+1 and nums[j] == nums[j-1]:
    #                 continue
    #             if nums[i] + nums[j] > 0:
    #                 break
    #             for k in range(j+1, n):
    #                 if k > j+1 and nums[k] == nums[k-1]:
    #                     continue
    #                 if nums[i] + nums[j] + nums[k] == 0:
    #                     ans.append([nums[i], nums[j], nums[k]])

    #     return ans


        
# @lc code=end



#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#

