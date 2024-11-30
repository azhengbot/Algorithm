#
# @lc app=leetcode.cn id=106 lang=python3
# @lcpr version=30204
#
# [106] 从中序与后序遍历序列构造二叉树
#
# https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (72.54%)
# Likes:    1285
# Dislikes: 0
# Total Accepted:    431.4K
# Total Submissions: 594.6K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder
# 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。
#
#
#
# 示例 1:
#
# 输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# 输出：[3,9,20,null,null,15,7]
#
#
# 示例 2:
#
# 输入：inorder = [-1], postorder = [-1]
# 输出：[-1]
#
#
#
#
# 提示:
#
#
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder 和 postorder 都由 不同 的值组成
# postorder 中每一个值都在 inorder 中
# inorder 保证是树的中序遍历
# postorder 保证是树的后序遍历
#
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
from typing import List


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return
        root = TreeNode(postorder[-1])
        if len(inorder) == 1:
            return root
        root_index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index + 1 :], postorder[root_index:-1])

        return root


# @lc code=end


#
# @lcpr case=start
# [9,3,15,20,7]\n[9,15,7,20,3]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#
