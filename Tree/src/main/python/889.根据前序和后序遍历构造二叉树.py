#
# @lc app=leetcode.cn id=889 lang=python3
#
# [889] 根据前序和后序遍历构造二叉树
#
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
#
# algorithms
# Medium (67.86%)
# Likes:    365
# Dislikes: 0
# Total Accepted:    52.8K
# Total Submissions: 76.1K
# Testcase Example:  '[1,2,4,5,3,6,7]\n[4,5,2,6,7,3,1]'
#
# 给定两个整数数组，preorder 和 postorder ，其中 preorder 是一个具有 无重复 值的二叉树的前序遍历，postorder
# 是同一棵树的后序遍历，重构并返回二叉树。
# 
# 如果存在多个答案，您可以返回其中 任何 一个。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# 输出：[1,2,3,4,5,6,7]
# 
# 
# 示例 2:
# 
# 
# 输入: preorder = [1], postorder = [1]
# 输出: [1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= preorder.length <= 30
# 1 <= preorder[i] <= preorder.length
# preorder 中所有值都 不同
# postorder.length == preorder.length
# 1 <= postorder[i] <= postorder.length
# postorder 中所有值都 不同
# 保证 preorder 和 postorder 是同一棵二叉树的前序遍历和后序遍历
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
from typing import List, Optional


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        left_size = postorder.index(preorder[1]) + 1

        left = self.constructFromPrePost(preorder[1: 1+left_size], postorder[:left_size])
        right = self.constructFromPrePost(preorder[1+left_size:], postorder[left_size: -1])

        return TreeNode(preorder[0], left, right)
# @lc code=end

