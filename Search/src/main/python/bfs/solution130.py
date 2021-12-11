from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        to = [[] for _ in range(m * n)]

        dx = [1, 0, 0, -1]
        dy = [0, 1, -1, 0]

        zero_border = []

        board_map = {}

        used = [False for _ in range(m * n)]
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and (
                    board[i][j] == "O"
                ):
                    zero_border.append(n * i + j)

                board_map[n * i + j] = (i, j)

                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]

                    if nx < 0 or ny < 0 or nx >= m or ny >= n:
                        continue

                    if board[nx][ny] == board[i][j]:
                        to[n * nx + ny].append(n * i + j)

        for one_zero_border in zero_border:
            queue = []
            used[one_zero_border] = True
            queue.append(one_zero_border)

            while len(queue) != 0:
                first = queue.pop(0)

                for can_to in to[first]:
                    if used[can_to]:
                        continue

                    used[can_to] = True
                    queue.append(can_to)

        for i in range(m):
            for j in range(n):
                if used[n * i + j]:
                    continue
                else:
                    board[i][j] = "X"


s = Solution()
board = [
    ["X", "O", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "O", "O", "X"],
    ["X", "O", "X", "X"],
]
s.solve(board)