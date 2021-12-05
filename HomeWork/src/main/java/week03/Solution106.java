package week03;

import common.TreeNode;

public class Solution106 {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        this.inorder = inorder;
        this.postorder = postorder;
        return build(0, inorder.length - 1, 0, postorder.length - 1);

    }

    private TreeNode build(int il, int ir, int pl, int pr) {

        if (il > ir) {
            return null;
        }

        TreeNode root = new TreeNode(postorder[pr]);

        for (int i = il; i <= ir; i++) {
            if (inorder[i] == postorder[pr]) {
                TreeNode left = build(il, i - 1, pl, pl + i - il - 1);
                TreeNode right = build(i + 1, ir, pr - ir + i, pr - 1);

                root.left = left;
                root.right = right;
            }

        }
        return root;

    }

    private int[] inorder;
    private int[] postorder;

    public static void main(String[] args) {
        Solution106 s = new Solution106();
        // int[] inorder = { 9, 3, 15, 20, 7 };
        // int[] postorder = { 9, 15, 7, 20, 3 };
        int[] inorder = { 2, 1 };
        int[] postorder = { 2, 1 };
        s.buildTree(inorder, postorder);
    }
}
