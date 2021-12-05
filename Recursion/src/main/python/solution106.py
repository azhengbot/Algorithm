# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(inorder, postorder):
            if len(inorder) == 0:
                return None

            root = TreeNode(postorder[-1])

            for i in range(len(inorder)):
                if inorder[i] == postorder[-1]:
                    left = build(inorder=inorder[0:i], postorder=postorder[0:i])
                    right = build(
                        inorder=inorder[i + 1 :],
                        postorder=postorder[i : len(postorder) - 1],
                    )

                    root.left = left
                    root.right = right

            return root

        return build(inorder, postorder)
