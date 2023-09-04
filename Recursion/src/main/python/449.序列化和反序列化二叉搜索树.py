#
# @lc app=leetcode.cn id=449 lang=python3
#
# [449] 序列化和反序列化二叉搜索树
#
# https://leetcode.cn/problems/serialize-and-deserialize-bst/description/
#
# algorithms
# Medium (60.51%)
# Likes:    453
# Dislikes: 0
# Total Accepted:    53.3K
# Total Submissions: 86.8K
# Testcase Example:  '[2,1,3]'
#
# 序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。
#
# 设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。
# 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。
#
# 编码的字符串应尽可能紧凑。
#
#
#
# 示例 1：
#
#
# 输入：root = [2,1,3]
# 输出：[2,1,3]
#
#
# 示例 2：
#
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
# 树中节点数范围是 [0, 10^4]
# 0 <= Node.val <= 10^4
# 题目数据 保证 输入的树是一棵二叉搜索树。
#
#
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from typing import Optional


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        lst = []

        def dfs(node):
            if node is None:
                # node.append("")
                return
            dfs(node.left)
            dfs(node.right)
            lst.append(node.val)

        dfs(root)
        # print(lst, "-----")
        return ",".join([str(i) for i in lst])

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if not data:
            return None
        lst = [int(i) for i in data.split(",")]
        print(lst)

        def construct(lower, upper):
            if lst == [] or lst[-1] < lower or lst[-1] > upper:
                return None
            val = lst.pop()
            root = TreeNode(val)
            root.right = construct(val, upper)
            root.left = construct(lower, val)

            return root

        return construct(-inf, inf)


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# @lc code=end
