from distutils.command.build_scripts import first_line_re
from typing import List


class Solution:
    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:

        dx = [1, 0, 0, -1]
        dy = [0, 1, -1, 0]

        m = len(maze)
        n = len(maze[0])

        to = [[] for _ in range(m * n)]

        for i in range(m):
            for j in range(n):
                for t in range(4):
                    if maze[i][j] == 1:
                        continue
                    ni = i + dx[t]
                    nj = j + dy[t]
                    if ni < 0 or nj < 0 or ni >= m or nj >= n:
                        continue
                    if maze[ni][nj] == 1:
                        continue

                    to[i * n + j].append(ni * n + nj)

        queue = []
        start_res = start[0] * n + start[1]
        destination_res = destination[0] * n + destination[1]
        queue.append(start_res)

        used = [False for _ in range(m * n)]

        while len(queue) != 0:
            first = queue.pop(0)
            used[first] = True

            for can_to in to[first]:
                if used[can_to]:
                    continue
                if destination_res == can_to:
                    for destination_can_to in to[destination_res]:
                        if (
                            destination_can_to - destination_res == n
                            or destination_can_to - destination_res == 1
                        ):
                            return False

                    return True

                queue.append(can_to)

        return False


s = Solution()
# maze = [
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0],
#     [1, 1, 0, 1, 1],
#     [0, 0, 0, 0, 0],
# ]
# start = [0, 4]
# destination = [4, 4]

maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
start = [0, 4]
destination = [3, 2]
res = s.hasPath(maze, start, destination)
print(res)
