package dfs;

import java.util.*;

public class Solution17 {

    public List<String> letterCombinations(String digits) {

        if (digits.equals("")) {
            return new ArrayList<>();
        }

        this.n = digits.length();
        this.digits = digits;

        search(0);
        return ans;
    }

    private void search(int idx) {
        if (idx == n) {
            ans.add(s.toString());
            return;
        }

        for (char i : map.get(digits.toCharArray()[idx]).toCharArray()) {
            s = s.append(i);
            search(idx + 1);
            s.deleteCharAt(s.length() - 1);

        }

    }

    private String digits;
    private StringBuffer s = new StringBuffer();
    private List<String> ans = new ArrayList<>();
    private int n;
    private HashMap<Character, String> map = new HashMap<Character, String>() {
        {
            put('2', "abc");
            put('3', "def");
            put('4', "ghi");
            put('5', "jkl");
            put('6', "mno");
            put('7', "pqrs");
            put('8', "tuv");
            put('9', "wxyz");

        }
    };

    public static void main(String[] args) {
        Solution17 s = new Solution17();

        // String digits = "23";
        String digits = "";
        System.out.println(s.letterCombinations(digits));
    }
}
