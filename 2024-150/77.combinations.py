#
# @lc app=leetcode.cn id=77 lang=python3
# @lcpr version=30204
#
# [77] 组合
#
# https://leetcode.cn/problems/combinations/description/
#
# algorithms
# Medium (77.38%)
# Likes:    1701
# Dislikes: 0
# Total Accepted:    801.9K
# Total Submissions: 1M
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
#
# 你可以按 任何顺序 返回答案。
#
#
#
# 示例 1：
#
# 输入：n = 4, k = 2
# 输出：
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
# 示例 2：
#
# 输入：n = 1, k = 1
# 输出：[[1]]
#
#
#
# 提示：
#
#
# 1 <= n <= 20
# 1 <= k <= n
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        sub_ans = []
        used = [0] * (n + 1)

        def dfs(i):
            if i >= k:
                ans.append(sub_ans[:])
                return

            for j in range(1, n + 1):
                if used[j]:
                    continue
                if sub_ans and j < sub_ans[-1]:
                    continue
                used[j] = 1
                sub_ans.append(j)
                dfs(i + 1)
                sub_ans.pop()
                used[j] = 0

        dfs(0)
        return ans


# @lc code=end


#
# @lcpr case=start
# 4\n2\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

#

#
