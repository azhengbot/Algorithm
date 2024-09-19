#
# @lc app=leetcode.cn id=2332 lang=python3
# @lcpr version=30204
#
# [2332] 坐上公交的最晚时间
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def latestTimeCatchTheBus(
        self, buses: List[int], passengers: List[int], capacity: int
    ) -> int:
        buses.sort()
        passengers.sort()
        m = len(passengers)
        i = 0

        for b in buses:
            c = capacity
            while c and i < m and passengers[i] <= b:
                i += 1
                c -= 1

        i -= 1

        ans = buses[-1] if c else passengers[i]
        while i >= 0 and ans == passengers[i]:
            i -= 1
            ans -= 1

        return ans


# @lc code=end

s = Solution()
res = s.latestTimeCatchTheBus([3], [2, 3], 2)
print(res)
res = s.latestTimeCatchTheBus([3], [2, 4], 2)
print(res)
res = s.latestTimeCatchTheBus([10, 20], [2, 17, 18, 19], 2)
print(res)
res = s.latestTimeCatchTheBus([20, 30, 10], [19, 13, 26, 4, 25, 11, 21], 2)
print(res)


#
# @lcpr case=start
# [10,20]\n[2,17,18,19]\n2\n
# @lcpr case=end

# @lcpr case=start
# [20,30,10]\n[19,13,26,4,25,11,21]\n2\n
# @lcpr case=end

#
