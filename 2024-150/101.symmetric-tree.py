#
# @lc app=leetcode.cn id=101 lang=python3
# @lcpr version=30204
#
# [101] 对称二叉树
#
# https://leetcode.cn/problems/symmetric-tree/description/
#
# algorithms
# Easy (61.29%)
# Likes:    2836
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 2M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
#
#
#
# 示例 1：
#
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
#
#
# 示例 2：
#
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [1, 1000] 内
# -100 <= Node.val <= 100
#
#
#
#
# 进阶：你可以运用递归和迭代两种方法解决这个问题吗？
#
#


# @lcpr-template-start

from collections import deque

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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        dq = deque()
        if (not root.left) and (not root.right):
            return True
        if root.left:
            dq.append(root.left)
        else:
            return False

        if root.right:
            dq.append(root.right)
        else:
            return False
        while dq:
            back = deque()
            if len(dq) % 2:
                return False

            n = len(dq)
            # print(len(dq), dq)
            i, j = 0, n - 1
            while i < j:
                if not dq[i] and not dq[j]:
                    i += 1
                    j -= 1
                    continue
                elif (not dq[i] and dq[j]) or (dq[i] and not dq[j]):
                    return False
                if dq[i].val != dq[j].val:
                    # print(dq[i].val, dq[j].val)
                    return False
                i += 1
                j -= 1
            for node in dq:
                if node:
                    back.append(node.left)
                    back.append(node.right)

            dq = back
        return True


# @lc code=end


#
# @lcpr case=start
# [1,2,2,3,4,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,3,4,5,5,4,null,null,8,9,9,8]\n
# @lcpr case=end

#
