# SWORD_OFFER
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#
# https://leetcode-cn.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (49.34%)
# Likes:    559
# Dislikes: 0
# Total Accepted:    57.5K
# Total Submissions: 116.4K
# Testcase Example:  '"aab"'
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
# 
# 返回符合要求的 最少分割次数 。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "aab"
# 输出：1
# 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "a"
# 输出：0
# 
# 
# 示例 3：
# 
# 
# 输入：s = "ab"
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 仅由小写英文字母组成
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
# @lc code=end

