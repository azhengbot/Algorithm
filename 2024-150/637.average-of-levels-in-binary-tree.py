#
# @lc app=leetcode.cn id=637 lang=python3
# @lcpr version=30204
#
# [637] 二叉树的层平均值
#
# https://leetcode.cn/problems/average-of-levels-in-binary-tree/description/
#
# algorithms
# Easy (71.18%)
# Likes:    502
# Dislikes: 0
# Total Accepted:    223.8K
# Total Submissions: 314.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个非空二叉树的根节点 root , 以数组的形式返回每一层节点的平均值。与实际答案相差 10^-5 以内的答案可以被接受。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[3.00000,14.50000,11.00000]
# 解释：第 0 层的平均值为 3,第 1 层的平均值为 14.5,第 2 层的平均值为 11 。
# 因此返回 [3, 14.5, 11] 。
#
#
# 示例 2:
#
#
#
# 输入：root = [3,9,20,15,7]
# 输出：[3.00000,14.50000,11.00000]
#
#
#
#
# 提示：
#
#
#
#
# 树中节点数量在 [1, 10^4] 范围内
# -2^31 <= Node.val <= 2^31 - 1
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import List, Optional


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        dq = deque([root])
        ans_lst = []
        while dq:
            n = len(dq)
            ans = 0
            for _ in range(n):
                node = dq.popleft()
                ans += node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

            ans_lst.append(ans / n)

        return ans_lst


# @lc code=end


#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [3,9,20,15,7]\n
# @lcpr case=end

#
