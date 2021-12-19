from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(piles, h, k):
            use_hour = 0

            for pile in piles:
                # while pile > k:
                #     use_hour += 1
                #     pile -= k
                if k == 0:
                    return False
                need_hour = math.ceil(pile / k)

                use_hour += need_hour

                if use_hour > h:
                    return False

            return use_hour <= h

        left = 0
        right = sum(piles)

        while left < right:
            mid = (left + right) // 2

            if check(piles, h, mid):
                right = mid
            else:
                left = mid + 1

        return right


s = Solution()
# piles = [312884470]
# h = 312884469
piles = [312884470]
h = 968709470
res = s.minEatingSpeed(piles=piles, h=h)
print(res)
