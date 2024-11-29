#
# @lc app=leetcode.cn id=102 lang=python3
# @lcpr version=30204
#
# [102] 二叉树的层序遍历
#
# https://leetcode.cn/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (68.45%)
# Likes:    2044
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 1.7M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
#
#
#
# 示例 1：
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
#
#
# 示例 2：
#
# 输入：root = [1]
# 输出：[[1]]
#
#
# 示例 3：
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
# 树中节点数目在范围 [0, 2000] 内
# -1000 <= Node.val <= 1000
#
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq = deque([root])
        res = []

        while dq:
            ans = []

            n = len(dq)
            for _ in range(n):
                node = dq.popleft()
                ans.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            # print(ans)
            res.append(ans)
        return res


# @lc code=end


#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
