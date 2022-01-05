import java.util.HashMap;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution337 {

    private HashMap<TreeNode, int[]> opt;

    public int rob(TreeNode root) {
        opt = new HashMap<TreeNode, int[]>();
        opt.put(null, new int[] { 0, 0 });
        dfs(root);

        return Math.max(opt.get(root)[0], opt.get(root)[1]);
    }

    private void dfs(TreeNode node) {
        if (node == null)
            return;

        opt.put(node, new int[2]);

        dfs(node.left);
        dfs(node.right);

        opt.get(node)[0] = Math.max(
                opt.get(node.left)[0], opt.get(node.left)[1])
                + Math.max(
                        opt.get(node.right)[0], opt.get(node.right)[1]);
        opt.get(node)[1] = opt.get(node.left)[0] + node.val + opt.get(node.right)[0];

    }
}
