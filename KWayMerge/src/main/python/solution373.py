from typing import List
import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:

        n1 = len(nums1)
        n2 = len(nums2)
        rever = False

        if n1 > n2:
            n1, n2 = n2, n1
            nums1, nums2 = nums2, nums1
            rever = True

        hq = []
        ans = []

        for i in range(min(n1, k)):
            heapq.heappush(hq, [nums1[i] + nums2[0], i, 0])

        while len(ans) < k and hq:
            _, i, j = heapq.heappop(hq)
            ans.append([nums1[i], nums2[j]] if not rever else [nums2[j], nums1[i]])

            if j + 1 < n2:
                heapq.heappush(hq, [nums1[i] + nums2[j + 1], i, j + 1])
        return ans


s = Solution()
nums1 = [6, 7, 11]
nums2 = [2, 4, 6]
k = 3
res = s.kSmallestPairs(nums1, nums2, k)
