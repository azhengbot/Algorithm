package BST;

/*
 * lang=java
 *
 * 面试题 04.06. 后继者
 *
 * https://leetcode-cn.com/problems/successor-lcci/
 *
 *
 * 设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。
 *
 * 如果指定节点没有对应的“下一个”节点，则返回null。
 *
 * 示例：
 *
 * 输入: root = [2,1,3], p = 1
 * 输出: 2
 *
 *
 *
 * 输入: root = [5,3,6,2,4,null,null,1], p = 6
 * 输出: null
 *
 *
 */

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        return findSuccessor(root, p.val);
    }

    private TreeNode findSuccessor(TreeNode root, int val) {
        TreeNode succ = null;
        while (root != null) {
            if (val < root.val) {
                if (succ == null || root.val < succ.val) {
                    succ = root;
                }
                root = root.left;
            } else if (val > root.val) {
                root = root.right;
            } else {
                if (root.right != null) {
                    succ = root.right;
                    while (succ.left != null) {
                        succ = succ.left;
                    }
                }
                break;
            }
        }
        return succ;

    }
}