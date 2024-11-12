#
# @lc app=leetcode.cn id=22 lang=python3
# @lcpr version=30204
#
# [22] 括号生成
#
# https://leetcode.cn/problems/generate-parentheses/description/
#
# algorithms
# Medium (78.22%)
# Likes:    3717
# Dislikes: 0
# Total Accepted:    931K
# Total Submissions: 1.2M
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
# 示例 1：
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#
#
# 示例 2：
#
# 输入：n = 1
# 输出：["()"]
#
#
#
#
# 提示：
#
#
# 1 <= n <= 8
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sub_ans = []
        ans = []

        def dfs(i, cnt):
            nonlocal sub_ans
            # print(ans, sub_ans)

            if cnt > 0:
                return
            if cnt < -n:
                return
            if i >= 2 * n:
                if cnt == 0:
                    ans.append("".join(sub_ans))
                # sub_ans = []
                return

            sub_ans.append(")")
            dfs(i + 1, cnt + 1)
            sub_ans.pop()

            sub_ans.append("(")
            dfs(i + 1, cnt - 1)
            sub_ans.pop()

        dfs(0, 0)
        return ans


# @lc code=end


#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#
