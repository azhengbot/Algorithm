#
# @lc app=leetcode.cn id=56 lang=python3
# @lcpr version=30204
#
# [56] 合并区间
#
# https://leetcode.cn/problems/merge-intervals/description/
#
# algorithms
# Medium (50.66%)
# Likes:    2461
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 2M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]
# 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
#
#
#
# 示例 1：
#
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
#
# 示例 2：
#
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
#
#
#
# 提示：
#
#
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []

        for start, end in intervals:
            if not ans:
                ans.append([start, end])
                continue

            pre_start, pre_end = ans.pop()

            if start <= pre_end:
                if end <= pre_end:
                    ans.append([pre_start, pre_end])
                    continue
                elif end > pre_end:
                    ans.append([pre_start, end])
                    continue

            ans.append([pre_start, pre_end])
            ans.append([start, end])

        return ans


# @lc code=end


#
# @lcpr case=start
# [[1,3],[2,6],[8,10],[15,18]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,4],[4,5]]\n
# @lcpr case=end

#
