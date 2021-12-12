
import common.TreeNode;

public class Solution528 {
    int sum = 0;

    public TreeNode convertBST(TreeNode root) {
        dfs(root);
        return root;

    }

    private void dfs(TreeNode root) {
        if (root != null) {
            dfs(root.right);
            sum = sum + root.val;
            root.val = sum;
            dfs(root.left);
        }

        return;

    }

    public static void main(String[] args) {
        Solution528 s = new Solution528();
        TreeNode root = new TreeNode(4);
        TreeNode left = new TreeNode(3);
        TreeNode right = new TreeNode(6);
        TreeNode rightLeft = new TreeNode(5);
        TreeNode rightRight = new TreeNode(7);

        right.left = rightLeft;
        right.right = rightRight;

        root.left = left;
        root.right = right;
        s.convertBST(root);

    }

}
