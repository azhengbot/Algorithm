# SWORD_OFFER
# @lc app=leetcode.cn id=926 lang=python3
#
# [926] 将字符串翻转到单调递增
#
# https://leetcode-cn.com/problems/flip-string-to-monotone-increasing/description/
#
# algorithms
# Medium (54.60%)
# Likes:    146
# Dislikes: 0
# Total Accepted:    9.6K
# Total Submissions: 17.3K
# Testcase Example:  '"00110"'
#
# 如果一个由 '0' 和 '1' 组成的字符串，是以一些 '0'（可能没有 '0'）后面跟着一些 '1'（也可能没有
# '1'）的形式组成的，那么该字符串是单调递增的。
# 
# 我们给出一个由字符 '0' 和 '1' 组成的字符串 S，我们可以将任何 '0' 翻转为 '1' 或者将 '1' 翻转为 '0'。
# 
# 返回使 S 单调递增的最小翻转次数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "00110"
# 输出：1
# 解释：我们翻转最后一位得到 00111.
# 
# 
# 示例 2：
# 
# 
# 输入：s = "010110"
# 输出：2
# 解释：我们翻转得到 011111，或者是 000111。
# 
# 
# 示例 3：
# 
# 
# 输入：s = "00011000"
# 输出：2
# 解释：我们翻转得到 00000000。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^5
# S 中只包含字符 '0' 和 '1'
# 
# 
#

# @lc code=start
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
# @lc code=end

