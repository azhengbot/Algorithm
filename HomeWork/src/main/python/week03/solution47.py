from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        res = []
        ans = []
        nums = sorted(nums)

        def recur(pos):
            if pos == len(nums):
                res.append(ans[:])
                return

            for i in range(len(nums)):
                if i > 0 and nums[i - 1] == nums[i] and used[i - 1] == False:
                    continue
                if used[i] != True:
                    ans.append(nums[i])
                    used[i] = True
                    recur(pos + 1)
                    used[i] = False
                    ans.pop()

        recur(0)
        return res


s = Solution()
# nums = [1, 2, 3]
nums = [1, 1, 2]
res = s.permuteUnique(nums=nums)
print(res)