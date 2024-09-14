#
# @lc app=leetcode.cn id=2390 lang=python3
# @lcpr version=30204
#
# [2390] 从字符串中移除星号
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "*":
                stack.pop()
                continue
            stack.append(c)

        return "".join(stack)


# @lc code=end


#
# @lcpr case=start
# "leet**cod*e"\n
# @lcpr case=end

# @lcpr case=start
# "erase*****"\n
# @lcpr case=end

#
