from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = sorted(nums, reverse=True)

        # return nums[k-1]

        n = len(nums)

        def partition(l, r):
            pivot = random.randrange(l, r)
            pivot_val = nums[pivot]

            while l <= r:
                while nums[l] < pivot_val:
                    l += 1
                while nums[r] > pivot_val:
                    r -= 1

                if l == r:
                    break

                if l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1

            return r

        idx = n - k

        def quick_sort(l: int, r: int):
            if l >= r:
                return nums[l]
            pivot = partition(l, r)

            if idx <= pivot:
                return quick_sort(l, pivot)
            else:
                return quick_sort(pivot + 1, r)

        return quick_sort(0, n - 1)


s = Solution()
# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
nums = [2, 1, 5, 4, 3]
k = 4
res = s.findKthLargest(nums, k)
print(res)
