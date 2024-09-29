#
# @lc app=leetcode.cn id=2516 lang=python3
# @lcpr version=30204
#
# [2516] 每种字符至少取 K 个
#
# https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/description/
#
# algorithms
# Medium (41.36%)
# Likes:    83
# Dislikes: 0
# Total Accepted:    16.9K
# Total Submissions: 36.2K
# Testcase Example:  '"aabaaaacaabc"\n2'
#
# 给你一个由字符 'a'、'b'、'c' 组成的字符串 s 和一个非负整数 k 。每分钟，你可以选择取走 s 最左侧 还是 最右侧 的那个字符。
#
# 你必须取走每种字符 至少 k 个，返回需要的 最少 分钟数；如果无法取到，则返回 -1 。
#
#
#
# 示例 1：
#
# 输入：s = "aabaaaacaabc", k = 2
# 输出：8
# 解释：
# 从 s 的左侧取三个字符，现在共取到两个字符 'a' 、一个字符 'b' 。
# 从 s 的右侧取五个字符，现在共取到四个字符 'a' 、两个字符 'b' 和两个字符 'c' 。
# 共需要 3 + 5 = 8 分钟。
# 可以证明需要的最少分钟数是 8 。
#
#
# 示例 2：
#
# 输入：s = "a", k = 1
# 输出：-1
# 解释：无法取到一个字符 'b' 或者 'c'，所以返回 -1 。
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 10^5
# s 仅由字母 'a'、'b'、'c' 组成
# 0 <= k <= s.length
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

from collections import Counter


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = Counter(s)
        if any(cnt[v] < k for v in "abc"):
            return -1

        i = 0
        ans = 0
        for j, c in enumerate(s):
            cnt[c] -= 1
            while cnt[c] < k:
                cnt[s[i]] += 1
                i += 1
            ans = max(ans, j - i + 1)

        return len(s) - ans


# aabaaaacaabc
# aabaa
# cbaac


# @lc code=end


#
# @lcpr case=start
# "aabaaaacaabc"\n2\n
# @lcpr case=end

# @lcpr case=start
# "a"\n1\n
# @lcpr case=end

#
#
#
#
