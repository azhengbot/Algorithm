#
# @lc app=leetcode.cn id=14 lang=python3
# @lcpr version=30204
#
# [14] 最长公共前缀
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x: len(x))
        if not strs:
            return ""
        ans = strs[0]

        n = len(strs)

        for i in range(1, n):
            b = strs[i]
            m = min(len(ans), len(b))
             
            for j in range(m):
                if ans[j] != b[j]:
                    if j == 0:
                        return ""
                    ans = ans[:j]
                    break
        return ans
# @lc code=end



#
# @lcpr case=start
# ["flower","flow","flight"]\n
# @lcpr case=end

# @lcpr case=start
# ["dog","racecar","car"]\n
# @lcpr case=end

#

