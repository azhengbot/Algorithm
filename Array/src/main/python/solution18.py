from typing import List


# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

#         sub_ans = []
#         ans = []

#         nums = sorted(nums)

#         def dfs(idx):

#             if len(sub_ans) == 4:
#                 if sum(sub_ans) == target:
#                     sorted_sub_ans = sub_ans[:]
#                     if sorted_sub_ans in ans:
#                         return
#                     ans.append(sorted_sub_ans)
#                 return

#             if idx >= len(nums) or len(sub_ans) + len(nums) - idx < 4:
#                 return
#             # if idx >= len(nums):
#             #     return

#             # if nums[idx + 1] == nums[idx]:
#             #     return

#             sub_ans.append(nums[idx])
#             dfs(idx + 1)
#             sub_ans.pop()
#             # if idx + 1 < len(nums) and last == nums[idx + 1]:
#             #     return
#             dfs(idx + 1)

#         dfs(0)

#         return ans


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)

        n = len(nums)
        res = []

        def twoSum(two_start, two_left_target):
            two_sum_res = []
            # other_set = set()
            for i in range(two_start, n):

                if i > two_start and nums[i] == nums[i - 1]:
                    continue
                if i + 1 < n and two_left_target - nums[i] in set(nums[i + 1 :]):
                    two_sum_res.append([nums[i], two_left_target - nums[i]])
            return two_sum_res

        def threeSum(start, left_tree_target):
            three_sum_res = []
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                two_left_target = left_tree_target - nums[i]
                two_sum_res = twoSum(i + 1, two_left_target)

                for sub_two_sum_res in two_sum_res:
                    sub_two_sum_res.append(nums[i])
                    three_sum_res.append(sub_two_sum_res)

            return three_sum_res

        for i in range(n - 3):
            left_tree_target = target - nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            three_sum_res = threeSum(i + 1, left_tree_target)

            for sub_three_sum_res in three_sum_res:
                sub_three_sum_res.append(nums[i])
                res.append(sub_three_sum_res)

        return res


s = Solution()
# nums = [1, 0, -1, 0, -2, 2]
# target = 0
# nums = [2, 2, 2, 2, 2]
# target = 8
# nums = [3, 4, 5, 5, 5, 6, 6]
# target = 20
nums = [0, 0, 0, 0]
target = 0
res = s.fourSum(nums=nums, target=target)
print(res)
