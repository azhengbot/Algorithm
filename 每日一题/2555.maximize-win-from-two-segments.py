#
# @lc app=leetcode.cn id=2555 lang=python3
# @lcpr version=30204
#
# [2555] 两个线段获得的最多奖品
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        left = 0
        mx = [0] * (n + 1)
        ans = 0
        if k * 2 + 1 >= prizePositions[n - 1] - prizePositions[0]:
            return n
        for right, pp in enumerate(prizePositions):
            while pp - prizePositions[left] > k:
                left += 1

            ans = max(ans, mx[left] + right - left + 1)
            mx[right + 1] = max(mx[right], right - left + 1)
        return ans


# @lc code=end


#
# @lcpr case=start
# [1,1,2,2,3,3,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n0\n
# @lcpr case=end

#
