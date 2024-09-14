#
# @lc app=leetcode.cn id=2576 lang=python3
# @lcpr version=30204
#
# [2576] 求出最多标记下标
#


# @lcpr-template-start


from bisect import bisect_left

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        check = lambda x: any(nums[i] * 2 > nums[i - x - 1] for i in range(x + 1))

        return bisect_left(range(len(nums) // 2), True, key=check) * 2


# 2, 4, 5, 9
# 4, 8, 10, 18

# 2, 3, 4, 5
# 4, 6, 8, 10

# @lc code=end


#
# @lcpr case=start
# [3,5,2,4]\n
# @lcpr case=end

# @lcpr case=start
# [9,2,5,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,8]\n
# @lcpr case=end

#
