#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#
# https://leetcode.cn/problems/invert-binary-tree/description/
#
# algorithms
# Easy (79.91%)
# Likes:    1762
# Dislikes: 0
# Total Accepted:    798.4K
# Total Submissions: 998.3K
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：root = [2,1,3]
# 输出：[2,3,1]
# 
# 
# 示例 3：
# 
# 
# 输入：root = []
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目范围在 [0, 100] 内
# -100 <= Node.val <= 100
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            mid = node.left
            node.left = node.right
            node.right = mid
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root

# @lc code=end

