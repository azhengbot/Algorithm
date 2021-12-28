from typing import List

# https://leetcode-cn.com/problems/maximum-product-subarray/


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        opt = [[float("INF"), float("-INF")] for _ in range(n)]

        opt[0] = [nums[0], nums[0]]

        for i in range(1, n):
            opt[i][0] = min(opt[i - 1][0] * nums[i], opt[i - 1][1] * nums[i], nums[i])
            opt[i][1] = max(opt[i - 1][0] * nums[i], opt[i - 1][1] * nums[i], nums[i])

        # print(opt)
        return max(sum(opt, []))
