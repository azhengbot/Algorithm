#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30204
#
# [20] 有效的括号
#
# https://leetcode.cn/problems/valid-parentheses/description/
#
# algorithms
# Easy (44.30%)
# Likes:    4581
# Dislikes: 0
# Total Accepted:    2M
# Total Submissions: 4.5M
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
#
#
#
#
# 示例 1：
#
#
# 输入：s = "()"
#
# 输出：true
#
#
# 示例 2：
#
#
# 输入：s = "()[]{}"
#
# 输出：true
#
#
# 示例 3：
#
#
# 输入：s = "(]"
#
# 输出：false
#
#
# 示例 4：
#
#
# 输入：s = "([])"
#
# 输出：true
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 10^4
# s 仅由括号 '()[]{}' 组成
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {"(": ")", "[": "]", "{": "}"}

        for c in s:
            if not stack:
                if c in (")", "]", "}"):
                    return False
                stack.append(c)
                continue
            if c in dic:
                stack.append(c)
                continue
            if dic[stack.pop()] != c:
                return False

        return not stack


# @lc code=end


#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

#
