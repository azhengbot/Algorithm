#
# @lc app=leetcode.cn id=100 lang=python3
# @lcpr version=30204
#
# [100] 相同的树
#
# https://leetcode.cn/problems/same-tree/description/
#
# algorithms
# Easy (62.41%)
# Likes:    1186
# Dislikes: 0
# Total Accepted:    632K
# Total Submissions: 1M
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
#
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
#
#
#
# 示例 1：
#
# 输入：p = [1,2,3], q = [1,2,3]
# 输出：true
#
#
# 示例 2：
#
# 输入：p = [1,2], q = [1,null,2]
# 输出：false
#
#
# 示例 3：
#
# 输入：p = [1,2,1], q = [1,1,2]
# 输出：false
#
#
#
#
# 提示：
#
#
# 两棵树上的节点数目都在范围 [0, 100] 内
# -10^4 <= Node.val <= 10^4
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
from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if p and q and p.val != q.val:
            return False
        if (not p and q) or (not q and p):
            return False
        return (
            p
            and q
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )


# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n[1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[1,null,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1]\n[1,1,2]\n
# @lcpr case=end

#

#
