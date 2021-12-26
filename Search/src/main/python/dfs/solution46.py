from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        used = [False for i in range(n)]
        chosen = []

        ans = []

        def dfs(position):
            if position >= n:
                ans.append(chosen[:])
                return

            for idx, num in enumerate(nums):
                if used[idx]:
                    continue

                chosen.append(num)
                used[idx] = True

                dfs(position + 1)

                used[idx] = False
                chosen.pop()

        dfs(0)

        return ans


s = Solution()
nums = [1, 2, 3]
res = s.permute(nums)

print(res)
