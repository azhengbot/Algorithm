#
# @lc app=leetcode.cn id=207 lang=python3
# @lcpr version=30204
#
# [207] 课程表
#
# https://leetcode.cn/problems/course-schedule/description/
#
# algorithms
# Medium (54.66%)
# Likes:    2057
# Dislikes: 0
# Total Accepted:    483.2K
# Total Submissions: 883.9K
# Testcase Example:  '2\n[[1,0]]'
#
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
#
# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi]
# ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
#
#
# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
#
#
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
#
# 示例 2：
#
# 输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
# 输出：false
# 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
#
#
#
# 提示：
#
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# prerequisites[i] 中的所有课程对 互不相同
#
#
#


# @lcpr-template-start

from collections import deque

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        deg = [0] * numCourses
        used = [0] * numCourses

        for x, y in prerequisites:
            graph[y].append(x)
            deg[x] += 1

        dq = deque([])

        for i, d in enumerate(deg):
            if d == 0:
                dq.append(i)
                used[i] = 1

        if not len(dq):
            return False

        while dq:
            course = dq.popleft()

            for nex_course in graph[course]:
                deg[nex_course] -= 1
                if deg[nex_course] == 0:
                    dq.append(nex_course)
                    used[nex_course] = 1

        return all(used)


# @lc code=end


#
# @lcpr case=start
# 2\n[[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[1,0],[0,1]]\n
# @lcpr case=end

#
