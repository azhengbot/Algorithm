#
# @lc app=leetcode.cn id=79 lang=python3
# @lcpr version=30204
#
# [79] 单词搜索
#
# https://leetcode.cn/problems/word-search/description/
#
# algorithms
# Medium (47.76%)
# Likes:    1900
# Dislikes: 0
# Total Accepted:    597.4K
# Total Submissions: 1.2M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#
#
# 示例 1：
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "ABCCED"
# 输出：true
#
#
# 示例 2：
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "SEE"
# 输出：true
#
#
# 示例 3：
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "ABCB"
# 输出：false
#
#
#
#
# 提示：
#
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board 和 word 仅由大小写英文字母组成
#
#
#
#
# 进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        used = [[False] * n for _ in range(m)]
        # len(word)
        to = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(i, j, k):
            # print(i, j, board[i][j], k)
            if k == len(word) - 1:
                return True
            for x, y in to:
                ni = i + x
                nj = j + y
                if ni >= m or nj >= n or ni < 0 or nj < 0:
                    continue
                if word[k + 1] != board[ni][nj]:
                    continue
                if used[ni][nj]:
                    continue
                used[ni][nj] = True
                res = dfs(ni, nj, k + 1)
                used[ni][nj] = False

                if res:
                    return True
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    used[i][j] = True
                    res = dfs(i, j, 0)
                    if res:
                        return True
                    used[i][j] = False
        return False


# @lc code=end


#
# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"\n
# @lcpr case=end

# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"SEE"\n
# @lcpr case=end

# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCB"\n
# @lcpr case=end

# @lcpr case=start
# [["a","a"]]\n"aaa"\n
# @lcpr case=end

#
