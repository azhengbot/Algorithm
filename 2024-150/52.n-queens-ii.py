# TODO
# @lc app=leetcode.cn id=52 lang=python3
# @lcpr version=30204
#
# [52] N 皇后 II
#
# https://leetcode.cn/problems/n-queens-ii/description/
#
# algorithms
# Hard (82.44%)
# Likes:    528
# Dislikes: 0
# Total Accepted:    163.2K
# Total Submissions: 197.9K
# Testcase Example:  '4'
#
# n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。
#
#
#
#
#
# 示例 1：
#
# 输入：n = 4
# 输出：2
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#
#
# 示例 2：
#
# 输入：n = 1
# 输出：1
#
#
#
#
# 提示：
#
#
# 1 <= n <= 9
#
#
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        col = [False] * n
        dia = [False] * 2 * n
        rev_dia = [False] * 2 * n

        def dfs(r):
            nonlocal ans

            if r == n:
                ans += 1
                return

            for c in range(n):
                if col[c] or dia[r + c] or rev_dia[r - c]:
                    continue
                col[c] = True
                dia[c + r] = True
                rev_dia[r - c] = True
                dfs(r + 1)
                rev_dia[r - c] = False
                dia[r + c] = False
                col[c] = False

        dfs(0)

        return ans


# 0, 1, 2, 3
# 4, 5, 6, 7
# 8, 9, 10, 11
# 12, 13, 14, 15

# (0, 0), (0, 1), (0, 2), (0, 3)
# (1, 0), (1, 1), (1, 2), (1, 3)
# (2, 0), (2, 1), (2, 2), (2, 3)
# (3, 0), (3, 1), (3, 2), (3, 3)
# @lc code=end


#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#
