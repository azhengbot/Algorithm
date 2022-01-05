# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        opt = {}
        opt[None] = [0, 0]

        def dfs(node):
            if node == None:
                return

            opt[node] = [0, 0]
            dfs(node.right)
            dfs(node.left)

            opt[node][0] = max(opt.get(node.right)[0], opt.get(node.right)[1]) + max(  # type: ignore
                opt.get(node.left)[0], opt.get(node.left)[1]  # type: ignore
            )
            opt[node][1] = opt.get(node.right)[0] + node.val + opt.get(node.left)[0]  # type: ignore

        dfs(root)

        # print(opt)
        return max(opt.get(root))
