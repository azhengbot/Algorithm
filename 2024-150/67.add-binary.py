#
# @lc app=leetcode.cn id=67 lang=python3
# @lcpr version=30204
#
# [67] 二进制求和
#
# https://leetcode.cn/problems/add-binary/description/
#
# algorithms
# Easy (53.49%)
# Likes:    1254
# Dislikes: 0
# Total Accepted:    432.5K
# Total Submissions: 808K
# Testcase Example:  '"11"\n"1"'
#
# 给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
#
#
#
# 示例 1：
#
# 输入:a = "11", b = "1"
# 输出："100"
#
# 示例 2：
#
# 输入：a = "1010", b = "1011"
# 输出："10101"
#
#
#
# 提示：
#
#
# 1 <= a.length, b.length <= 10^4
# a 和 b 仅由字符 '0' 或 '1' 组成
# 字符串如果不是 "0" ，就不含前导零
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        i, j = m - 1, n - 1
        ans = []
        flag = 0
        while i >= 0 or j >= 0 or flag:
            if i < 0:
                x = 0
            else:
                x = a[i]
            if j < 0:
                y = 0
            else:
                y = b[j]
            c = int(x) + int(y) + flag
            if c >= 2:
                flag = 1
                ans.insert(0, str(c - 2))
            else:
                flag = 0
                ans.insert(0, str(c))

            i -= 1
            j -= 1

        return "".join(ans)


# @lc code=end


#
# @lcpr case=start
# "11"\n"1"\n
# @lcpr case=end

# @lcpr case=start
# "1010"\n"1011"\n
# @lcpr case=end

#
