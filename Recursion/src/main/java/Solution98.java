
import common.TreeNode;

public class Solution98 {
    public boolean isValidBST(TreeNode root) {
        // 需要将边界 +1
        boolean res = check(root, Integer.MIN_VALUE - 1l, Integer.MAX_VALUE + 1l);
        return res;
    }

    private boolean check(TreeNode node, long leftMin, long rightMax) {
        if (node == null) {
            return true;
        }
        System.out.println(node.val);
        System.out.println(rightMax);
        System.out.println(node.val - rightMax);

        if (node.val > leftMin && node.val < rightMax) {
            return check(node.right, node.val, rightMax) && check(node.left, leftMin, node.val);
        }

        return false;
    }

}
