#
# @lc app=leetcode.cn id=228 lang=python3
# @lcpr version=30204
#
# [228] 汇总区间
#
# https://leetcode.cn/problems/summary-ranges/description/
#
# algorithms
# Easy (54.84%)
# Likes:    416
# Dislikes: 0
# Total Accepted:    193.2K
# Total Submissions: 352.2K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# 给定一个  无重复元素 的 有序 整数数组 nums 。
#
# 返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于
# nums 的数字 x 。
#
# 列表中的每个区间范围 [a,b] 应该按如下格式输出：
#
#
# "a->b" ，如果 a != b
# "a" ，如果 a == b
#
#
#
#
# 示例 1：
#
# 输入：nums = [0,1,2,4,5,7]
# 输出：["0->2","4->5","7"]
# 解释：区间范围是：
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
#
#
# 示例 2：
#
# 输入：nums = [0,2,3,4,6,8,9]
# 输出：["0","2->4","6","8->9"]
# 解释：区间范围是：
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
#
#
#
#
# 提示：
#
#
# 0 <= nums.length <= 20
# -2^31 <= nums[i] <= 2^31 - 1
# nums 中的所有值都 互不相同
# nums 按升序排列
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if not nums:
            return []

        start = nums[0]
        n = len(nums)
        if n == 1:
            return [str(nums[0])]
        for i in range(1, n):
            if nums[i] - nums[i - 1] != 1:
                if nums[i - 1] == start:
                    ans.append(f"{start}")
                else:
                    ans.append(f"{start}->{nums[i-1]}")

                start = nums[i]
            if i == n - 1:
                if nums[i] == start:
                    ans.append(f"{start}")
                else:
                    ans.append(f"{start}->{nums[i]}")
        return ans


# @lc code=end


#
# @lcpr case=start
# [0,1,2,4,5,7]\n
# @lcpr case=end

# @lcpr case=start
# [0,2,3,4,6,8,9]\n
# @lcpr case=end

#
