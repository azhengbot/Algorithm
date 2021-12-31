from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        n: int = len(nums)

        opt: List[List[int]] = [[float("-inf"), float("-inf")] for _ in range(n)]

        opt[0][0] = 0
        opt[0][1] = nums[0]

        for i in range(1, n):
            opt[i][0] = max(opt[i - 1][0], opt[i - 1][1])
            opt[i][1] = opt[i - 1][0] + nums[i]

        print(opt)
        return max(opt[n - 1])
