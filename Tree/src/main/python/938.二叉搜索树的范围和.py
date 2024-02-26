#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#
# https://leetcode.cn/problems/range-sum-of-bst/description/
#
# algorithms
# Easy (82.11%)
# Likes:    359
# Dislikes: 0
# Total Accepted:    140.6K
# Total Submissions: 169.7K
# Testcase Example:  '[10,5,15,3,7,null,18]\n7\n15'
#
# 给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
# 输出：32
# 
# 
# 示例 2：
# 
# 
# 输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# 输出：23
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [1, 2 * 10^4] 内
# 1 
# 1 
# 所有 Node.val 互不相同
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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0

        def dfs(root):
            nonlocal ans
            if not root:
                return
            if low <= root.val <= high:
                ans += root.val

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ans
            
# @lc code=end

