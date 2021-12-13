from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return
        ans = []

        def get_in_order(root):
            if root.right == None:
                ans.append(root.val)
                if root.left:
                    get_in_order(root.left)
                return

            if root.right:
                get_in_order(root.right)

            ans.append(root.val)

            if root.left:
                get_in_order(root.left)

        get_in_order(root)
        pre_sum = [0 for _ in range(len(ans) + 1)]
        for i in range(1, len(ans) + 1):
            pre_sum[i] = pre_sum[i - 1] + ans[i - 1]

        res_map = dict(zip(ans, pre_sum[1:]))

        def change_vale(root):
            if root == None:
                return

            root.val = res_map.get(root.val)

            if root.right:
                change_vale(root.right)
            if root.left:
                change_vale(root.left)

        change_vale(root)
        return root