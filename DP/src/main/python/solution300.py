from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        opt = [1 for _ in range(n)]

        for i in range(n):
            for j in range(i + 1):
                if nums[i] > nums[j]:
                    opt[i] = max(opt[j] + 1, opt[i])

        # print(opt)
        return max(opt)
