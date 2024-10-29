# TODO
# @lc app=leetcode.cn id=205 lang=python3
# @lcpr version=30204
#
# [205] 同构字符串
#
# https://leetcode.cn/problems/isomorphic-strings/description/
#
# algorithms
# Easy (49.59%)
# Likes:    740
# Dislikes: 0
# Total Accepted:    305.6K
# Total Submissions: 615.5K
# Testcase Example:  '"egg"\n"add"'
#
# 给定两个字符串 s 和 t ，判断它们是否是同构的。
#
# 如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
#
#
# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
#
#
#
# 示例 1:
#
# 输入：s = "egg", t = "add"
# 输出：true
#
#
# 示例 2：
#
# 输入：s = "foo", t = "bar"
# 输出：false
#
# 示例 3：
#
# 输入：s = "paper", t = "title"
# 输出：true
#
#
#
# 提示：
#
#
#
#
# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s 和 t 由任意有效的 ASCII 字符组成
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if m != n:
            return False
        dic1 = {}
        dic2 = {}

        for i, c in enumerate(s):
            if c in dic1 or t[i] in dic2:
                if dic1.get(c) == t[i] and dic2.get(t[i]) == c:
                    continue
                return False
            dic1[c] = t[i]
            dic2[t[i]] = c

        return True


# @lc code=end
# "badc"
# "baba"

#
# @lcpr case=start
# "badc"\n"baba"\n
# @lcpr case=end

# @lcpr case=start
# "foo"\n"bar"\n
# @lcpr case=end

# @lcpr case=start
# "paper"\n"title"\n
# @lcpr case=end

#
