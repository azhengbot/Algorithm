# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return

        if root.val == key:
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left

            next = root.right

            while next.left:
                next = next.left

            root.right = self.deleteNode(root.right, next.val)
            root.val = next.val

            return root

        if root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:
            root.left = self.deleteNode(root.left, key)

        return root
