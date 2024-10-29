#
# @lc app=leetcode.cn id=199 lang=python3
# @lcpr version=30204
#
# [199] 二叉树的右视图
#
# https://leetcode.cn/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (67.98%)
# Likes:    1130
# Dislikes: 0
# Total Accepted:    497.6K
# Total Submissions: 730.2K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
#
#
# 示例 1:
#
#
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
#
#
# 示例 2:
#
# 输入: [1,null,3]
# 输出: [1,3]
#
#
# 示例 3:
#
# 输入: []
# 输出: []
#
#
#
#
# 提示:
#
#
# 二叉树的节点个数的范围是 [0,100]
# -100 <= Node.val <= 100
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
from typing import List, Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        dq = [root]
        ans = []
        while dq:
            new_dq = []
            ans.append(dq[-1].val)
            for node in dq:
                if node.left:
                    new_dq.append(node.left)
                if node.right:
                    new_dq.append(node.right)
            dq = new_dq
        return ans


# @lc code=end


#
# @lcpr case=start
# [1,2,3,null,5,null,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
