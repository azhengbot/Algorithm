from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)

        pre_sum = [0] * (length + 1)

        for i in range(1, length + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]

        pre_min = [pre_sum[0]] * (length + 1)

        for i in range(1, length + 1):
            pre_min[i] = min(pre_sum[i], pre_min[i - 1])

        ans = nums[0]
        for i in range(1, length + 1):
            ans = max(ans, pre_sum[i] - pre_min[i - 1])

        return ans


s = Solution()
res = s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(res)
