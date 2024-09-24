#
# @lc app=leetcode.cn id=2207 lang=python3
# @lcpr version=30204
#
# [2207] 字符串中最多数目的子序列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        cnt1 = cnt2 = 0
        ans = 0
        for i, c in enumerate(text):
            if c == pattern[0]:
                cnt1 += 1
            elif c == pattern[1]:
                cnt2 += 1
                ans += cnt1

        if cnt1 == cnt2 == 0:
            return 0

        if cnt1 == 0 or cnt2 == 0:
            if pattern[0] == pattern[1]:
                cnt = cnt1 or cnt2
                for i in range(1, cnt + 1):
                    ans += i

                return ans
            else:
                return cnt1 or cnt2

        if cnt1 < cnt2:
            ans += cnt2
        else:
            ans += cnt1

        return ans


# rozsjqzottomeiytlvkenctevztfjlgszlv
# tttctt

# @lc code=end


#
# @lcpr case=start
# "abdcdbc"\n"ac"\n
# @lcpr case=end

# @lcpr case=start
# "aabb"\n"ab"\n
# @lcpr case=end

#
