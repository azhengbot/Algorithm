# https://leetcode-cn.com/problems/subsets/

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.sub_ans = []
        self.recur(0, nums)

        return self.ans

    def recur(self, n, nums):
        if n == len(nums):
            # 需要做个切片
            self.ans.append(self.sub_ans[:])
            return

        self.recur(n + 1, nums)

        self.sub_ans.append(nums[n])

        self.recur(n + 1, nums)

        self.sub_ans.pop()


s = Solution()
nums = [1, 2, 3]
# nums = [0]
res = s.subsets(nums)

print(res)