import common.TreeNode;

public class Solution450 {
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) {
            return null;
        }

        if (root.val == key) {
            if (root.left == null) {
                // root = root.right;
                // 要直接返回， 否则，下面的可以能也进行了赋值
                return root.right;
            }
            if (root.right == null) {
                // root = root.left;
                return root.left;
            }

            TreeNode next = root.right;

            while (next.left != null) {
                next = next.left;
            }

            // 要赋值，否则会改变结构
            root.right = deleteNode(root.right, next.val);

            root.val = next.val;
            return root;
        }

        if (root.val < key) {
            root.right = deleteNode(root.right, key);
        } else {
            root.left = deleteNode(root.left, key);
        }

        return root;
    }
}
