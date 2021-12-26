from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        opt = [0 for i in range(n)]

        opt[0] = nums[0]

        for i in range(1, n):
            opt[i] = max(opt[i - 1] + nums[i], nums[i])

        # print(opt)
        return max(opt)
