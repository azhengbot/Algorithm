#
# @lc app=leetcode.cn id=5 lang=python3
# @lcpr version=30204
#
# [5] 最长回文子串
#
# https://leetcode.cn/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (38.73%)
# Likes:    7390
# Dislikes: 0
# Total Accepted:    1.8M
# Total Submissions: 4.7M
# Testcase Example:  '"babad"'
#
# 给你一个字符串 s，找到 s 中最长的 回文 子串。
#
#
#
# 示例 1：
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#
#
# 示例 2：
#
# 输入：s = "cbbd"
# 输出："bb"
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1

            return s[i + 1 : j]

        res = ""
        for i in range(n):
            res1 = expand(i, i)
            res2 = expand(i, i + 1)

            res = max(res, res1, res2, key=len)

        return res


# @lc code=end


#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#
