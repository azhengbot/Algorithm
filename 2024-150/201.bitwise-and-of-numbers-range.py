# TODO
# @lc app=leetcode.cn id=201 lang=python3
# @lcpr version=30204
#
# [201] 数字范围按位与
#
# https://leetcode.cn/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (55.02%)
# Likes:    533
# Dislikes: 0
# Total Accepted:    101.6K
# Total Submissions: 184.6K
# Testcase Example:  '5\n7'
#
# 给你两个整数 left 和 right ，表示区间 [left, right] ，返回此区间内所有数字 按位与 的结果（包含 left 、right
# 端点）。
#
#
#
# 示例 1：
#
# 输入：left = 5, right = 7
# 输出：4
#
#
# 示例 2：
#
# 输入：left = 0, right = 0
# 输出：0
#
#
# 示例 3：
#
# 输入：left = 1, right = 2147483647
# 输出：0
#
#
#
#
# 提示：
#
#
# 0 <= left <= right <= 2^31 - 1
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = left
        for i in range(left + 1, right + 1):
            ans &= i
        return ans


# @lc code=end


#
# @lcpr case=start
# 5\n7\n
# @lcpr case=end

# @lcpr case=start
# 0\n0\n
# @lcpr case=end

# @lcpr case=start
# 1\n2147483647\n
# @lcpr case=end

#
