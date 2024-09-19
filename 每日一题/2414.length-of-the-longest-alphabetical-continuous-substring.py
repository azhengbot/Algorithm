#
# @lc app=leetcode.cn id=2414 lang=python3
# @lcpr version=30204
#
# [2414] 最长的字母序连续子字符串的长度
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        i, j = 0, 0
        n = len(s)
        ans = 1

        while j < n:
            if j > 0 and (ord(s[j]) - ord(s[j - 1]) != 1):
                ans = max(ans, j - i)
                i = j
            j += 1
        ans = max(ans, j - i)
        return ans


# @lc code=end


#
# @lcpr case=start
# "abacaba"\n
# @lcpr case=end

# @lcpr case=start
# "abcde"\n
# @lcpr case=end

#
