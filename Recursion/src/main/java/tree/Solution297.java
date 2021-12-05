package tree;

import common.TreeNode;
import java.util.*;

public class Solution297 {
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        List<String> seq = new ArrayList<>();
        dfs(seq, root);
        return String.join(",", seq);
    }

    private void dfs(List<String> seq, TreeNode root) {
        if (root == null) {
            seq.add("null");
            return;
        }
        seq.add(Integer.toString(root.val));
        dfs(seq, root.left);
        dfs(seq, root.right);

    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        seq = data.split(",");
        curr = 0;

        return restore();
    }

    private TreeNode restore() {
        if (seq[curr].equals("null")) {
            curr++;
            return null;
        }

        TreeNode root = new TreeNode(Integer.parseInt(seq[curr]));
        curr++;
        root.left = restore();
        root.right = restore();
        return root;
    }

    private String[] seq;
    private Integer curr;
}
