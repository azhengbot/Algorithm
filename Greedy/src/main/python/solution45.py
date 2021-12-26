from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        n: int = len(nums)
        i: int = 0

        count: int = 0

        while i < n:
            if i == n - 1:
                return count
            # if nums[i] == 0:
            #     ...

            next_to = 0
            first_to = 0
            for to in range(nums[i] + 1):
                if to == 0:
                    continue
                cur_first_to = i + to

                if cur_first_to >= n - 1:
                    count += 1
                    return count
                cur_next_to = cur_first_to + nums[i + to]

                if cur_first_to >= n - 1:
                    count += 2
                    return count

                if cur_next_to > next_to:
                    next_to = cur_next_to
                    first_to = cur_first_to

            i = first_to
            count += 1

        return count


s = Solution()
nums = [1, 2]
nums = [0]
# nums = [1, 1, 1, 1]
# nums = [1, 2, 1, 1, 1]
# nums = [2, 3, 0, 1, 4]
# nums = [2, 3, 1, 1, 4]
# nums = [2, 1]
# nums = [2, 3, 1]
# nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]

res = s.jump(nums=nums)
print(res)
