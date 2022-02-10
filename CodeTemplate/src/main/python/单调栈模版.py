#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (43.63%)
# Likes:    1743
# Dislikes: 0
# Total Accepted:    210.1K
# Total Submissions: 481.3K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
# 示例 1:
#
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
#
# 示例 2：
#
# 输入： heights = [2,4]
# 输出： 4
# 提示：
# 1
# 0

# @lc code=start
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)  # 帮助我们在最后把栈清空
        stack = []  # [[height, width], ...]
        ans = 0
        # 每个柱子入栈、出栈各一次，2n=O(n)
        # 第一步：for 每个元素
        for height in heights:
            accumulate_width = 0
            # 第二步：while (栈顶不满足高度单调性) 累加宽度，出栈
            while len(stack) != 0 and stack[-1][0] > height:
                top = stack.pop()
                accumulate_width += top[1]
                ans = max(ans, top[0] * accumulate_width)
            # 第三步：新元素入栈
            stack.append((height, accumulate_width + 1))

        return ans


# @lc code=end
