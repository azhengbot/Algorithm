from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        ans = [-1, -1]
        while left < right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        if right >= 0 and nums[right] == target:
            ans[0] = right

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right + 1) // 2

            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1

        if right >= 0 and nums[right] == target:
            ans[1] = right

        return ans