from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        to = [[] for i in range(numCourses)]

        in_deg = [0] * numCourses

        for pre in prerequisites:
            ai = pre[0]
            bi = pre[1]
            to[bi].append(ai)
            in_deg[ai] += 1

        q = []

        for i in range(numCourses):
            if in_deg[i] == 0:
                q.append(i)

        lessons = []

        while len(q) != 0:
            x = q[0]
            q.pop(0)
            lessons.append(x)

            for y in to[x]:
                in_deg[y] -= 1
                if in_deg[y] == 0:
                    q.append(y)

        return len(lessons) == numCourses


s = Solution()
# numCourses = 20
# prerequisites = [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]
numCourses = 5
prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]

res = s.canFinish(numCourses, prerequisites)
print(res)