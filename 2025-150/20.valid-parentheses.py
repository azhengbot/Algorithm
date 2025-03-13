#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30204
#
# [20] 有效的括号
#
# https://leetcode.cn/problems/valid-parentheses/description/
#
# algorithms
# Easy (44.61%)
# Likes:    4667
# Dislikes: 0
# Total Accepted:    2.1M
# Total Submissions: 4.7M
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
        dic = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if c not in dic:
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1] == dic.get(c):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


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
