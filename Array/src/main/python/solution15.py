from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        print(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            res = self.get_two_nums(nums, i + 1, -nums[i])
            print(res)

            for l in res:
                l.insert(0, nums[i])

                ans.append(l)

        return ans

    def get_two_nums(self, nums, start, target):
        j = len(nums) - 1
        i = start
        ans = []

        while i < len(nums):
            if i > start and nums[i] == nums[i - 1]:
                i += 1
                continue
            while i < j and nums[i] + nums[j] > target:
                j -= 1

            if j > i and nums[i] + nums[j] == target:
                ans.append([nums[i], nums[j]])

            i += 1
        return ans


s = Solution()
res = s.threeSum([-1, 0, 1, 2, -1, -4])
print(res)
