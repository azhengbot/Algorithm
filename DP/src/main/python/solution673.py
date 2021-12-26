from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        chosen = []
        ans = []
        # chosen[0] = nums[i]
        def dfs(i):

            if i >= n:
                ans.append(chosen[:])
                return

            if len(chosen) == 0 or nums[i] > chosen[-1]:
                chosen.append(nums[i])

            dfs(i + 1)
            chosen.pop()

            dfs(i + 1)
            # dfs(i+1)

        dfs(0)

        print(ans)


s = Solution()
nums = [1, 2, 4, 3, 5, 4, 7, 2]
s.findNumberOfLIS(nums)
