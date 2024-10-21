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
        ans = 1
        res = s[0]

        def check(i, j):
            while i < j and s[i] == s[j]:
                i += 1
                j -= 1

            return True if i == j or j < i else False

        for i in range(n):
            for j in range(i, n):
                if s[i] == s[j] and (j - i + 1 > ans) and check(i, j):
                    if j - i + 1 > ans:
                        res = s[i : j + 1]
                        ans = j - i + 1

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
