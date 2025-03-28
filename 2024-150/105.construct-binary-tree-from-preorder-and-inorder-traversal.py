#
# @lc app=leetcode.cn id=105 lang=python3
# @lcpr version=30204
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (72.18%)
# Likes:    2418
# Dislikes: 0
# Total Accepted:    742K
# Total Submissions: 1M
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder
# 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
#
#
#
# 示例 1:
#
# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]
#
#
# 示例 2:
#
# 输入: preorder = [-1], inorder = [-1]
# 输出: [-1]
#
#
#
#
# 提示:
#
#
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder 和 inorder 均 无重复 元素
# inorder 均出现在 preorder
# preorder 保证 为二叉树的前序遍历序列
# inorder 保证 为二叉树的中序遍历序列
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        root_index = inorder.index(preorder[0])
        # print(preorder, inorder, root_index)
        root.left = self.buildTree(preorder[1 : 1 + root_index], inorder[:root_index])
        if root_index + 1 >= len(preorder):
            return root
        root.right = self.buildTree(
            preorder[root_index + 1 :], inorder[root_index + 1 :]
        )

        return root


# @lc code=end


#
# @lcpr case=start
# [3,9,20,15,7]\n[9,3,15,20,7]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[2,1]\n
# @lcpr case=end

#
