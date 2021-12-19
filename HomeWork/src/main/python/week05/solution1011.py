from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(weights: List[int], days: int, box: int):
            day = 0
            has_weight = 0
            for weight in weights:
                has_weight += weight
                if has_weight > box:
                    day += 1
                    if day > days:
                        return False
                    has_weight = weight

            return day < days

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            if check(weights, days, mid):
                right = mid
            else:
                left = mid + 1

        return right
