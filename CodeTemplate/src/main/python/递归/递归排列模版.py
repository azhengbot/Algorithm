#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (78.49%)
# Likes:    1784
# Dislikes: 0
# Total Accepted:    519.9K
# Total Submissions: 662.4K
# Testcase Example:  '[1,2,3]'
#
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
# 示例 2：
#
#
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#
#
# 示例 3：
#
#
# 输入：nums = [1]
# 输出：[[1]]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# nums 中的所有整数 互不相同
#
#
#

# @lc code=start
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False for _ in range(n)]
        ans = []
        sub_ans = []

        def dfs(idx):
            if idx >= n:
                ans.append(sub_ans[:])
                return
            # 依次考虑0,1,...,n-1位置放哪个数
            # “从还没用过的”数中选一个放在当前位置
            for i in range(n):
                if used[i]:
                    continue

                sub_ans.append(nums[i])
                used[i] = True
                dfs(idx + 1)
                used[i] = False
                sub_ans.pop()

        dfs(0)
        return ans


s = Solution()
res = s.permute([1, 2, 3])
print(res)


# @lc code=end
