#
# @lc app=leetcode.cn id=530 lang=python3
# @lcpr version=30204
#
# [530] 二叉搜索树的最小绝对差
#
# https://leetcode.cn/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (62.85%)
# Likes:    586
# Dislikes: 0
# Total Accepted:    282.3K
# Total Submissions: 449.1K
# Testcase Example:  '[4,2,6,1,3]'
#
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
#
# 差值是一个正数，其数值等于两值之差的绝对值。
#
#
#
# 示例 1：
#
# 输入：root = [4,2,6,1,3]
# 输出：1
#
#
# 示例 2：
#
# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
#
#
#
#
# 提示：
#
#
# 树中节点的数目范围是 [2, 10^4]
# 0 <= Node.val <= 10^5
#
#
#
#
# 注意：本题与 783
# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        dfs(root)
        n = len(ans)
        res = float(inf)
        for i in range(1, n):
            res = min(res, ans[i] - ans[i - 1])
        return res


# @lc code=end


#
# @lcpr case=start
# [4,2,6,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,48,null,null,12,49]\n
# @lcpr case=end

#
