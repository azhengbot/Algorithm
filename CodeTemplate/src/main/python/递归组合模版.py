#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (76.97%)
# Likes:    872
# Dislikes: 0
# Total Accepted:    284.2K
# Total Submissions: 369.3K
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
#
# 输入：n = 1, k = 1
# 输出：[[1]]
#
#
#
# 提示：
#
#
# 1
# 1
#
#
#

# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sub_ans = []
        ans = []

        def dfs(idx):
            # 这种比下面的注释掉那种方法更快一些
            if idx > n + 1 or len(sub_ans) + (n - idx + 1) < k:
                return

            if len(sub_ans) == k:
                ans.append(sub_ans[:])
                return
            # if len(sub_ans) > k or len(sub_ans) + (n - idx + 1) < k:
            #     return

            # if idx > n:
            #     ans.append(sub_ans[:])

            dfs(idx + 1)

            sub_ans.append(idx)
            dfs(idx + 1)
            sub_ans.pop()

        dfs(1)
        return ans


# @lc code=end
