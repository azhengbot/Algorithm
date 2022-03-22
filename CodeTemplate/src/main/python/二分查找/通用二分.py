#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        # 开始位置（lower_bound）：查询第一个>=target的数
        # 范围 [0 .. n-1 ] + [n表示不存在]
        l = 0
        r = n

        while l < r:
            mid = (l + r) // 2

            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1  # 第一个>=target的数的下标（不存在为n）

        left = r

        # 结束位置：查询最后一个<=target的数
        # 范围 [-1表示不存在] + [0 .. n-1 ]
        l = -1
        r = n - 1

        while l < r:
            mid = (l + r + 1) // 2

            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1  # 最后一个<=target的数（不存在为-1）

        right = r

        # target出现在left, right
        if right < left:
            return [-1, -1]

        return [left, right]


# @lc code=end


# 实数二分模板
# ans = realSqrt(x, 1e-6)
# 如果要求4位小数，就多算2~4位，到1e-6或1e-8，保证精确


def realSqrt(x, eps=1e-6):
    left, right = 0, max(x, 1)
    while right - left > eps:
        mid = (left + right) / 2
        if mid * mid <= x:
            left = mid
        else:
            right = mid
    return right
