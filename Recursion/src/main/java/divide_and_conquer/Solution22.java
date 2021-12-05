package divide_and_conquer;

import java.util.*;

public class Solution22 {
    public List<String> generateParenthesis(int n) {

        List<String> ans = new ArrayList<>();

        if (n == 0) {
            ans.add("");
            return ans;
        }

        for (int i = 0; i < n; i++) {

            List<String> firstPart = generateParenthesis(i);
            List<String> secondPart = generateParenthesis(n - i - 1);

            for (String fp : firstPart) {
                for (String sp : secondPart) {
                    String res = "(" + fp + ")" + sp;
                    ans.add(res);
                }
            }
        }
        return ans;

    }

    public static void main(String[] args) {
        Solution22 s = new Solution22();
        List<String> res = s.generateParenthesis(3);

        System.out.println(res);
    }
}
