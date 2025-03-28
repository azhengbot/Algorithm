#
# @lc app=leetcode.cn id=58 lang=python3
# @lcpr version=30204
#
# [58] 最后一个单词的长度
#
# https://leetcode.cn/problems/length-of-last-word/description/
#
# algorithms
# Easy (46.81%)
# Likes:    724
# Dislikes: 0
# Total Accepted:    640.7K
# Total Submissions: 1.4M
# Testcase Example:  '"Hello World"'
#
# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
#
# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
#
#
#
# 示例 1：
#
# 输入：s = "Hello World"
# 输出：5
# 解释：最后一个单词是“World”，长度为 5。
#
#
# 示例 2：
#
# 输入：s = "   fly me   to   the moon  "
# 输出：4
# 解释：最后一个单词是“moon”，长度为 4。
#
#
# 示例 3：
#
# 输入：s = "luffy is still joyboy"
# 输出：6
# 解释：最后一个单词是长度为 6 的“joyboy”。
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 10^4
# s 仅有英文字母和空格 ' ' 组成
# s 中至少存在一个单词
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])


# @lc code=end


#
# @lcpr case=start
# "Hello World"\n
# @lcpr case=end

# @lcpr case=start
# "   fly me   to   the moon  "\n
# @lcpr case=end

# @lcpr case=start
# "luffy is still joyboy"\n
# @lcpr case=end

#
