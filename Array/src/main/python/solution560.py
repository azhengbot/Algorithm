from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        preSum = [0] * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]

        ans = 0

        # 超时了
        # for i in range(1, len(nums) + 1):
        #     for j in range(0, i):
        #         if preSum[i] - preSum[j] == k:
        #             ans += 1

        # 先存一下，避免超时
        cnt_map = {}

        for i in preSum:
            if cnt_map.get(i - k):
                ans += cnt_map.get(i - k)

            cnt = cnt_map.setdefault(i, 0)
            cnt += 1
            cnt_map[i] = cnt

        return ans