/*
 * @lc app=leetcode.cn id=106 lang=java
 *
 * [106] 从中序与后序遍历序列构造二叉树
 *
 * https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
 *
 * algorithms
 * Medium (72.29%)
 * Likes:    724
 * Dislikes: 0
 * Total Accepted:    184.7K
 * Total Submissions: 255.3K
 * Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
 *
 * 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder
 * 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 
 * 输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
 * 输出：[3,9,20,null,null,15,7]
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入：inorder = [-1], postorder = [-1]
 * 输出：[-1]
 * 
 * 
 * 
 * 
 * 提示:
 * 
 * 
 * 1 <= inorder.length <= 3000
 * postorder.length == inorder.length
 * -3000 <= inorder[i], postorder[i] <= 3000
 * inorder 和 postorder 都由 不同 的值组成
 * postorder 中每一个值都在 inorder 中
 * inorder 保证是树的中序遍历
 * postorder 保证是树的后序遍历
 * 
 * 
 */

// @lc code=start

import java.util.Arrays;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if (inorder.length == 0) {
            return null;
        }
        int rootValue = postorder[postorder.length - 1];
        TreeNode root = new TreeNode(rootValue);
        int idx = getIndex(inorder, rootValue);
        // System.out.println(Arrays.toString(inorder));
        // System.out.println(Arrays.toString(postorder));
        // System.out.println(rootValue);
        // System.out.println(idx);
        // System.out.println("------");
        root.left = buildTree(Arrays.copyOfRange(inorder, 0, idx), Arrays.copyOfRange(postorder, 0, idx));
        root.right = buildTree(Arrays.copyOfRange(inorder, idx + 1, inorder.length),
                Arrays.copyOfRange(postorder, idx, postorder.length - 1));

        return root;
    }

    private int getIndex(int[] inorder, int val) {
        int n = inorder.length;
        for (int i = 0; i < n; i++) {
            if (inorder[i] == val) {
                return i;
            }
        }
        return -1;
    }
}
// @lc code=end
