#
# @lc app=leetcode.cn id=1726 lang=python3
#
# [1726] 同积元组
#
# https://leetcode.cn/problems/tuple-with-same-product/description/
#
# algorithms
# Medium (52.36%)
# Likes:    59
# Dislikes: 0
# Total Accepted:    15.4K
# Total Submissions: 25.7K
# Testcase Example:  '[2,3,4,6]'
#
# 给你一个由 不同 正整数组成的数组 nums ，请你返回满足 a * b = c * d 的元组 (a, b, c, d) 的数量。其中 a、b、c 和
# d 都是 nums 中的元素，且 a != b != c != d 。
#
#
#
# 示例 1：
#
#
# 输入：nums = [2,3,4,6]
# 输出：8
# 解释：存在 8 个满足题意的元组：
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
#
#
# 示例 2：
#
#
# 输入：nums = [1,2,4,5,10]
# 输出：16
# 解释：存在 16 个满足题意的元组：
# (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
# (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
# (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,4,5)
# (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10^4
# nums 中的所有元素 互不相同
#
#
#

from collections import Counter

# @lc code=start
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = Counter()
        for i in range(n):
            for j in range(i + 1, n):
                cnt[nums[i] * nums[j]] += 1
        ans = 0
        for v in cnt.values():
            ans += v * (v - 1) * 4

        return ans
        # 超时
        # nums.sort()
        # sub_ans = []
        # ans = 0
        # n = len(nums)
        # used = [False for _ in range(n)]

        # def dfs(i, left):
        #     nonlocal ans
        #     if i == 3:
        #         if sub_ans[1] * sub_ans[2] % sub_ans[0]:
        #             return
        #     if i >= 4:
        #         if sub_ans[0] * sub_ans[3] == sub_ans[1] * sub_ans[2]:
        #             # ans.append(sub_ans[:])
        #             ans += 1
        #         return

        #     for j in range(left, n):
        #         if used[j]:
        #             continue
        #         sub_ans.append(nums[j])
        #         used[j] = True
        #         dfs(i + 1, j + 1)
        #         used[j] = False
        #         sub_ans.pop()

        # dfs(0, 0)

        # return ans * 8

        # 超时
        # ans: List[int] = []
        # nums.sort(reverse=True)
        # ans = 0
        # sub_ans: List[int] = []
        # n = len(nums)
        # used = [False for _ in range(n)]

        # def dfs(i):
        #     nonlocal ans
        #     if i == 3:
        #         if sub_ans[0] * sub_ans[1] % sub_ans[2]:
        #             return
        #     if i >= 4:
        #         if sub_ans[0] * sub_ans[1] == sub_ans[2] * sub_ans[3]:
        #             # ans.append(sub_ans[:])
        #             ans += 1
        #         return

        #     for j in range(n):
        #         if used[j]:
        #             continue

        #         sub_ans.append(nums[j])
        #         used[j] = True
        #         dfs(i + 1)
        #         used[j] = False
        #         sub_ans.pop()

        # dfs(0)
        # return ans


# @lc code=end
s = Solution()
nums = [69, 252, 95, 725, 112, 345, 390, 221, 405, 27, 58, 100, 392, 156, 147, 377, 32, 288, 350, 17, 230, 609, 29, 357, 66, 728, 140, 462, 190, 621, 51, 7, 475, 105, 255, 81, 391, 120, 690, 250, 308, 261, 68, 464, 28, 540, 116, 18, 192, 16, 468, 189, 532, 60, 56, 420, 207, 425, 630, 126, 40, 432, 2, 153, 84, 272, 870, 210, 552, 200, 228, 161, 285, 648, 322, 320, 132, 87, 459, 70, 336, 64, 184, 44, 338, 15, 196, 90, 117, 20, 14, 45, 266, 270, 374, 204, 133, 416, 165, 99, 780, 102, 551, 195, 34, 506, 182, 160, 513, 48, 114, 175, 72, 560, 494, 364, 22, 299, 225, 180, 460, 171, 104, 580, 476, 598, 4, 437, 150, 152, 76, 340, 650, 50, 145, 672, 522, 378, 75, 396, 12, 325, 375, 406, 21, 1, 170, 702, 10, 306, 348, 304, 224, 575, 418, 342, 696, 368, 24, 500, 483, 231, 203, 78, 399, 253, 26, 644, 174, 19, 54, 9, 486, 128, 567, 57, 720, 450, 8, 297, 162, 52, 96, 125, 588, 35, 456, 240, 30, 440, 260, 130, 594, 525, 91, 840, 154, 25, 330, 264]  # type: ignore


res = s.tupleSameProduct(nums)
print(res)
