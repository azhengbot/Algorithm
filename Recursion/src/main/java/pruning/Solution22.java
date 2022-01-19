package pruning;

import java.util.*;

public class Solution22 {
    public List<String> ans = new ArrayList<>();
    public StringBuilder subAns = new StringBuilder();
    public int n;

    public List<String> generateParenthesis(int n) {
        this.n = n;
        dfs(0, 0, 0);

        return ans;
    }

    private void dfs(int idx, int left, int right) {
        if (left > n || right > n || !check(subAns.toString())) {
            return;
        }
        if (idx == 2 * n) {

            ans.add(subAns.toString());

            return;
        }

        subAns.append("(");
        dfs(idx + 1, left + 1, right);
        subAns.deleteCharAt(subAns.length() - 1);

        subAns.append(")");
        dfs(idx + 1, left, right + 1);
        subAns.deleteCharAt(subAns.length() - 1);
    }

    private boolean check(String s) {
        int left = 0;

        for (char ch : s.toCharArray()) {
            if (ch == '(') {
                left++;
            } else {
                if (left == 0) {
                    return false;
                }
                left--;
            }
        }
        return true;
    }
}
