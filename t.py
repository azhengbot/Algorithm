from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        left = 1
        right = 1

        count = 1

        while right < n:
            if nums[right] == nums[right - 1]:
                right += 1
                continue
            else:
                nums[left] = nums[right]
                right += 1
                left += 1
                count += 1

        return count


s = Solution()
nums = [0, 1, 1, 1, 2, 2, 3]
res = s.removeDuplicates(nums)

print(res)
print(nums)
