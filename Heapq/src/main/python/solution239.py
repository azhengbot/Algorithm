from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq

        l = []
        res = []
        n = len(nums)

        ans = nums[0]
        for i in range(n):
            heapq.heappush(l, -nums[i])

            if i >= k - 1:
                ans = -l[0]
                while ans not in nums[i - k + 1 : i + 1]:
                    heapq.heappop(l)
                    ans = -l[0]

                res.append(ans)

        return res
