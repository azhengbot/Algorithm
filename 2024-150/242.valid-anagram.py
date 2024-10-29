#
# @lc app=leetcode.cn id=242 lang=python3
# @lcpr version=30204
#
# [242] 有效的字母异位词
#
# https://leetcode.cn/problems/valid-anagram/description/
#
# algorithms
# Easy (66.96%)
# Likes:    952
# Dislikes: 0
# Total Accepted:    859.1K
# Total Submissions: 1.3M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。
#
#
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#
#
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
#
#
#
# 提示:
#
#
# 1 <= s.length, t.length <= 5 * 10^4
# s 和 t 仅包含小写字母
#
#
#
#
# 进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        cnt_s = Counter(s)
        cnt_t = Counter(t)

        for k, v in cnt_s.items():
            if v != cnt_t[k]:
                return False

        return True


# @lc code=end


#
# @lcpr case=start
# "anagram"\n"nagaram"\n
# @lcpr case=end

# @lcpr case=start
# "rat"\n"car"\n
# @lcpr case=end

#
