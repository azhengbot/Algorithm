# https://leetcode-cn.com/problems/degree-of-an-array/

from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt_map = {}
        max_count = 0
        res = len(nums)

        for i in range(len(nums)):
            if cnt_map.get(nums[i]):
                cnt_map[nums[i]][1] += 1
            else:
                cnt_map[nums[i]] = [i, 1]

            if cnt_map[nums[i]][1] > max_count:
                max_count = cnt_map[nums[i]][1]

                res = i - cnt_map[nums[i]][0] + 1

            if cnt_map[nums[i]][1] == max_count:
                res = min(res, i - cnt_map[nums[i]][0] + 1)

        return res


s = Solution()
nums = [1, 2, 2, 3, 1]
res = s.findShortestSubArray(nums)

print(res)