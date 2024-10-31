#
# @lc app=leetcode.cn id=6 lang=python3
# @lcpr version=30204
#
# [6] Z 字形变换
#
# https://leetcode.cn/problems/zigzag-conversion/description/
#
# algorithms
# Medium (53.24%)
# Likes:    2392
# Dislikes: 0
# Total Accepted:    731K
# Total Submissions: 1.4M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
# string convert(string s, int numRows);
#
#
#
# 示例 1：
#
# 输入：s = "PAYPALISHIRING", numRows = 3
# 输出："PAHNAPLSIIGYIR"
#
# 示例 2：
#
# 输入：s = "PAYPALISHIRING", numRows = 4
# 输出："PINALSIGYAHRPI"
# 解释：
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
#
# 示例 3：
#
# 输入：s = "A", numRows = 1
# 输出："A"
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 1000
# s 由英文字母（小写和大写）、',' 和 '.' 组成
# 1 <= numRows <= 1000
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
[
    ["P", "", "A", "", "H"],
    ["A", "P", "L", "S", "I"],
    ["Y", "", "I", "", "R"],
]


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        num_cols = n * 2
        ans = [[""] * num_cols for _ in range(numRows)]
        i = 0
        for c in range(num_cols):
            if c % 2 == 0:
                for r in range(numRows):
                    if i >= n:
                        break
                    ans[r][c] = s[i]
                    i += 1
            else:
                for r in range(numRows - 2, 0, -1):
                    if i >= n:
                        break
                    ans[r][c] = s[i]
                    i += 1
        # print(ans)
        res = []

        for i in range(numRows):
            for j in range(num_cols):
                if ans[i][j]:
                    res.append(ans[i][j])
        return "".join(res)


# @lc code=end


#
# @lcpr case=start
# "PAYPALISHIRING"\n3\n
# @lcpr case=end

# @lcpr case=start
# "PAYPALISHIRING"\n4\n
# @lcpr case=end

# @lcpr case=start
# "ABCD"\n1\n
# @lcpr case=end

#
