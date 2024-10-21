#
# @lc app=leetcode.cn id=74 lang=python3
# @lcpr version=30204
#
# [74] 搜索二维矩阵
#
# https://leetcode.cn/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (50.26%)
# Likes:    975
# Dislikes: 0
# Total Accepted:    467.2K
# Total Submissions: 927.6K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# 给你一个满足下述两条属性的 m x n 整数矩阵：
#
#
# 每行中的整数从左到右按非严格递增顺序排列。
# 每行的第一个整数大于前一行的最后一个整数。
#
#
# 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
#
#
# 示例 2：
#
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True

        return False


# @lc code=end


#
# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n13\n
# @lcpr case=end

#
