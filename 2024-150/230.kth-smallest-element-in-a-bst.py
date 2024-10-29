# TODO
# @lc app=leetcode.cn id=230 lang=python3
# @lcpr version=30204
#
# [230] 二叉搜索树中第 K 小的元素
#
# https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (78.16%)
# Likes:    918
# Dislikes: 0
# Total Accepted:    432.8K
# Total Submissions: 552.7K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（从 1 开始计数）。
#
#
#
# 示例 1：
#
# 输入：root = [3,1,4,null,2], k = 1
# 输出：1
#
#
# 示例 2：
#
# 输入：root = [5,3,6,2,4,null,null,1], k = 3
# 输出：3
#
#
#
#
#
#
# 提示：
#
#
# 树中的节点数为 n 。
# 1 <= k <= n <= 10^4
# 0 <= Node.val <= 10^4
#
#
#
#
# 进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        res = None

        def dfs(node):
            nonlocal ans, res
            if not node:
                return
            if node.left:
                dfs(node.left)
            ans += 1

            if ans == k:
                res = node.val
                return

            if node.right:
                dfs(node.right)

        dfs(root)

        return res


# @lc code=end


#
# @lcpr case=start
# [3,1,4,null,2]\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,3,6,2,4,null,null,1]\n3\n
# @lcpr case=end

#

#
