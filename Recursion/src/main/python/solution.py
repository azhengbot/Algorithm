from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        sub_ans = []
        ans = []

        nums = sorted(nums)

        def dfs(idx):

            if len(sub_ans) == 4:
                if sum(sub_ans) == target:
                    sorted_sub_ans = sub_ans[:]
                    if sorted_sub_ans in ans:
                        return
                    ans.append(sorted_sub_ans)
                return

            if idx >= len(nums) or len(sub_ans) + len(nums) - idx < 4:
                return
            # if idx >= len(nums):
            #     return

            # if nums[idx + 1] == nums[idx]:
            #     return

            sub_ans.append(nums[idx])
            dfs(idx + 1)
            sub_ans.pop()
            # if idx + 1 < len(nums) and last == nums[idx + 1]:
            #     return
            dfs(idx + 1)

        dfs(0)

        return ans


s = Solution()
# nums = [1, 0, -1, 0, -2, 2]
# target = 0
# nums = [2, 2, 2, 2, 2]
# target = 8
nums = [3, 4, 5, 5, 5, 6, 6]
target = 20
res = s.fourSum(nums=nums, target=target)
print(res)
