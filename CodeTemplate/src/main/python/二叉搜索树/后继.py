#
# lang=python3
#
# 面试题 04.06. 后继者
#
# https://leetcode-cn.com/problems/successor-lcci/
#
#
# 设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。
#
# 如果指定节点没有对应的“下一个”节点，则返回null。
#

# 示例：
#
# 输入: root = [2,1,3], p = 1
# 输出: 2
#
#
#
# 输入: root = [5,3,6,2,4,null,null,1], p = 6
# 输出: null
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        return self.find_successor(root, p.val)

    def find_successor(self, root: TreeNode, val: int) -> TreeNode:
        succ = None
        while root:
            if val < root.val:
                # 或者在其经历过的节点中
                if (not succ) or root.val < succ.val:
                    succ = root
                root = root.left

            elif val > root.val:
                root = root.right

            else:
                # 如果有右子树， 在其右子树的最左子树
                if root.right:
                    succ = root.right
                    while succ.left:
                        succ = succ.left

                return succ
