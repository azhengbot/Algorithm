#
# @lc app=leetcode.cn id=826 lang=python3
#
# [826] 安排工作以达到最大收益
#
# https://leetcode.cn/problems/most-profit-assigning-work/description/
#
# algorithms
# Medium (43.53%)
# Likes:    140
# Dislikes: 0
# Total Accepted:    28K
# Total Submissions: 57.6K
# Testcase Example:  '[2,4,6,8,10]\n[10,20,30,40,50]\n[4,5,6,7]'
#
# 你有 n 个工作和 m 个工人。给定三个数组： difficulty, profit 和 worker ，其中:
# 
# 
# difficulty[i] 表示第 i 个工作的难度，profit[i] 表示第 i 个工作的收益。
# worker[i] 是第 i 个工人的能力，即该工人只能完成难度小于等于 worker[i] 的工作。
# 
# 
# 每个工人 最多 只能安排 一个 工作，但是一个工作可以 完成多次 。
# 
# 
# 举个例子，如果 3 个工人都尝试完成一份报酬为 $1 的同样工作，那么总收益为 $3 。如果一个工人不能完成任何工作，他的收益为 $0 。
# 
# 
# 返回 在把工人分配到工作岗位后，我们所能获得的最大利润 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
# 输出: 100 
# 解释: 工人被分配的工作难度是 [4,4,6,6] ，分别获得 [20,20,30,30] 的收益。
# 
# 示例 2:
# 
# 
# 输入: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
# 输出: 0
# 
# 
# 
# 提示:
# 
# 
# n == difficulty.length
# n == profit.length
# m == worker.length
# 1 <= n, m <= 10^4
# 1 <= difficulty[i], profit[i], worker[i] <= 10^5
# 
# 
#

from bisect import bisect_right
from collections import defaultdict

# @lc code=start
from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        di = sorted(difficulty)
        sort_d = sorted([(d, i) for i, d in enumerate(difficulty)])
        max_pro = 0
        max_d_map = defaultdict(int)
        for d, i in sort_d:
            if profit[i] > max_pro:
                max_pro = profit[i]
            max_d_map[d] = max_pro

        ans = 0

        for max_d in worker:
            idx = bisect_right(di, max_d)
            if idx == 0:
                continue
            ans += max_d_map.get(di[idx-1], 0)

        return ans

                




# @lc code=end

