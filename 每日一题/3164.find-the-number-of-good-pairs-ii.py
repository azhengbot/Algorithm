#
# @lc app=leetcode.cn id=3164 lang=python3
# @lcpr version=30204
#
# [3164] 优质数对的总数 II
#


# @lcpr-template-start

import math
from collections import defaultdict

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        dic = defaultdict(int)
        for x in nums1:
            if x % k:
                continue
            x = x // k
            for i in range(1, math.isqrt(x) + 1):
                if x % i == 0:
                    dic[i] += 1
                    if i * i < x:
                        dic[x // i] += 1

        return sum(dic[x] for x in nums2)


# @lc code=end


#
# @lcpr case=start
# [1,3,4]\n[1,3,4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,4,12]\n[2,4]\n3\n
# @lcpr case=end

#
