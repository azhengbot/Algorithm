from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            left_mid = (left + right) // 2
            right_mid = left_mid + 1

            if nums[left_mid] >= nums[right_mid]:
                right = left_mid

            else:
                left = left_mid + 1

        return right