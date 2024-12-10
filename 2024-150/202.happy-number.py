#
# @lc app=leetcode.cn id=202 lang=python3
# @lcpr version=30204
#
# [202] 快乐数
#
# https://leetcode.cn/problems/happy-number/description/
#
# algorithms
# Easy (64.99%)
# Likes:    1617
# Dislikes: 0
# Total Accepted:    575.5K
# Total Submissions: 884.2K
# Testcase Example:  '19'
#
# 编写一个算法来判断一个数 n 是不是快乐数。
#
# 「快乐数」 定义为：
#
#
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果这个过程 结果为 1，那么这个数就是快乐数。
#
#
# 如果 n 是 快乐数 就返回 true ；不是，则返回 false 。
#
#
#
# 示例 1：
#
# 输入：n = 19
# 输出：true
# 解释：
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
#
# 示例 2：
#
# 输入：n = 2
# 输出：false
#
#
#
#
# 提示：
#
#
# 1 <= n <= 2^31 - 1
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        used = set()
        while n:
            if n in used:
                return False
            if n == 1:
                return True
            used.add(n)
            b = n
            ans = 0
            while b:
                ans += (b % 10) ** 2
                b //= 10
            n = ans
        if n == 1:
            return True

        return False


# @lc code=end


#
# @lcpr case=start
# 19\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#
