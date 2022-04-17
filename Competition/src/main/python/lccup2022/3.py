from typing import Optional, List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getNumber(self, root: Optional[TreeNode], ops: List[List[int]]) -> int:
        ...


s = Solution()
# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.right = TreeNode(3)
# root.right.right.right = TreeNode(4)
# root.right.right.right.right = TreeNode(5)
# ops = [[1, 2, 4], [1, 1, 3], [0, 3, 5]]


root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)

root.right = TreeNode(7)
root.right.left = TreeNode(5)
root.right.left.right = TreeNode(6)
ops = [[0, 2, 2], [1, 1, 5], [0, 4, 5], [1, 5, 7]]
res = s.getNumber(root, ops)
print(res)
