#
# @lc app=leetcode.cn id=2127 lang=python3
#
# [2127] 参加会议的最多员工数
#
# https://leetcode.cn/problems/maximum-employees-to-be-invited-to-a-meeting/description/
#
# algorithms
# Hard (35.91%)
# Likes:    170
# Dislikes: 0
# Total Accepted:    11.2K
# Total Submissions: 22.6K
# Testcase Example:  '[2,2,1,2]'
#
# 一个公司准备组织一场会议，邀请名单上有 n 位员工。公司准备了一张 圆形 的桌子，可以坐下 任意数目 的员工。
#
# 员工编号为 0 到 n - 1 。每位员工都有一位 喜欢 的员工，每位员工 当且仅当 他被安排在喜欢员工的旁边，他才会参加会议。每位员工喜欢的员工 不会
# 是他自己。
#
# 给你一个下标从 0 开始的整数数组 favorite ，其中 favorite[i] 表示第 i 位员工喜欢的员工。请你返回参加会议的 最多员工数目
# 。
#
#
#
# 示例 1：
#
#
#
# 输入：favorite = [2,2,1,2]
# 输出：3
# 解释：
# 上图展示了公司邀请员工 0，1 和 2 参加会议以及他们在圆桌上的座位。
# 没办法邀请所有员工参与会议，因为员工 2 没办法同时坐在 0，1 和 3 员工的旁边。
# 注意，公司也可以邀请员工 1，2 和 3 参加会议。
# 所以最多参加会议的员工数目为 3 。
#
#
# 示例 2：
#
# 输入：favorite = [1,2,0]
# 输出：3
# 解释：
# 每个员工都至少是另一个员工喜欢的员工。所以公司邀请他们所有人参加会议的前提是所有人都参加了会议。
# 座位安排同图 1 所示：
# - 员工 0 坐在员工 2 和 1 之间。
# - 员工 1 坐在员工 0 和 2 之间。
# - 员工 2 坐在员工 1 和 0 之间。
# 参与会议的最多员工数目为 3 。
#
#
# 示例 3：
#
#
#
# 输入：favorite = [3,0,1,4,1]
# 输出：4
# 解释：
# 上图展示了公司可以邀请员工 0，1，3 和 4 参加会议以及他们在圆桌上的座位。
# 员工 2 无法参加，因为他喜欢的员工 0 旁边的座位已经被占领了。
# 所以公司只能不邀请员工 2 。
# 参加会议的最多员工数目为 4 。
#
#
#
#
# 提示：
#
#
# n == favorite.length
# 2 <= n <= 10^5
# 0 <= favorite[i] <= n - 1
# favorite[i] != i
#
#
#

from collections import deque

# @lc code=start
from typing import List


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        in_deg = [0] * n
        max_len = [0] * n
        for i, f in enumerate(favorite):
            in_deg[f] += 1

        dq = deque()
        for i in range(n):
            if not in_deg[i]:
                dq.append(i)

        while len(dq):
            i = dq.popleft()
            f = favorite[i]
            max_len[f] = max(max_len[f], max_len[i] + 1)
            in_deg[f] -= 1
            if in_deg[f] == 0:
                dq.append(f)

        ans1, ans2 = 0, 0

        for i in range(n):
            if not in_deg[i]:
                continue
            f = favorite[i]
            cur = 1
            while i != f:
                in_deg[f] = 0
                cur += 1
                f = favorite[f]

            if cur == 2:
                ans2 += 2 + max_len[i] + max_len[favorite[i]]
            else:
                ans1 = max(cur, ans1)

        return max(ans1, ans2)


# @lc code=end
