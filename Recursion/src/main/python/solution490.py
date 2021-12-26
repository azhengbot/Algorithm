from distutils.command.build_scripts import first_line_re
from typing import List

# TODO 没做出来
class Solution:
    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        ...


s = Solution()
maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
start = [0, 4]
destination = [4, 4]

# maze = [
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0],
#     [1, 1, 0, 1, 1],
#     [0, 0, 0, 0, 0],
# ]
# start = [0, 4]
# destination = [3, 2]
res = s.hasPath(maze, start, destination)
print(res)
