from typing import List


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        fa = list(range(n + 1))

        sz = [1] * (n + 1)

        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])

            return fa[x]

        q = sorted(zip(nums, range(n)), reverse=True)

        for num, i in q:

            f = find(i + 1)
            fa[i] = f
            sz[f] += sz[i]

            size = sz[f] - 1

            if num > threshold // size:
                return size

        return -1


s = Solution()
nums = [1, 3, 4, 3, 1]
threshold = 6
res = s.validSubarraySize(nums, threshold)
print(res)
