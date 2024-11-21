#
# @lc app=leetcode.cn id=57 lang=python3
# @lcpr version=30204
#
# [57] 插入区间
#
# https://leetcode.cn/problems/insert-interval/description/
#
# algorithms
# Medium (42.70%)
# Likes:    939
# Dislikes: 0
# Total Accepted:    237.6K
# Total Submissions: 556K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表 intervals，其中 intervals[i] = [starti, endi] 表示第 i
# 个区间的开始和结束，并且 intervals 按照 starti 升序排列。同样给定一个区间 newInterval = [start, end]
# 表示另一个区间的开始和结束。
#
# 在 intervals 中插入区间 newInterval，使得 intervals 依然按照 starti
# 升序排列，且区间之间不重叠（如果有必要的话，可以合并区间）。
#
# 返回插入之后的 intervals。
#
# 注意 你不需要原地修改 intervals。你可以创建一个新数组然后返回它。
#
#
#
# 示例 1：
#
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
#
#
# 示例 2：
#
# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
#
#
#
#
# 提示：
#
#
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^5
# intervals 根据 starti 按 升序 排列
# newInterval.length == 2
# 0 <= start <= end <= 10^5
#
#
#


# @lcpr-template-start

from bisect import bisect_left

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        n = len(intervals)
        start, end = newInterval
        i = bisect_left(intervals, newInterval)

        intervals.insert(i, newInterval)
        ans = []
        # print(intervals)
        for j in range(n + 1):
            if not ans:
                ans.append(intervals[j])
                continue
            pre_start, pre_end = ans.pop()
            start, end = intervals[j]
            if start <= pre_end:
                if end >= pre_end:
                    ans.append([pre_start, end])
                    continue
                elif end < pre_end:
                    ans.append([pre_start, pre_end])
                    continue
            ans.append([pre_start, pre_end])
            ans.append([start, end])
        # print(i, ans)

        return ans


# @lc code=end


#
# @lcpr case=start
# [[1,3],[6,9]]\n[2,5]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[3,5],[6,7],[8,10],[12,16]]\n[4,8]\n
# @lcpr case=end

#
