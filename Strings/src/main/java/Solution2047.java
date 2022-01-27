// https://leetcode-cn.com/problems/number-of-valid-words-in-a-sentence
public class Solution2047 {
    public int countValidWords(String sentence) {
        String[] tokenList = sentence.split(" ");
        int ans = 0;
        for (String token : tokenList) {
            if (checkToken(token)) {
                // System.out.println(token);
                ans++;
            }
        }
        return ans;

    }

    private boolean checkToken(String token) {
        int n = token.length();
        int hyphenCount = 0;
        if (n == 0)
            return false;
        for (int i = 0; i < n; i++) {
            if (Character.isDigit(token.charAt(i))) {
                return false;
            }
            if (token.charAt(i) == '-') {
                if (hyphenCount != 0 || i == 0 || i == n - 1 || !Character.isAlphabetic(token.charAt(i - 1))
                        || !Character.isAlphabetic(token.charAt(i + 1))) {
                    return false;
                } else {
                    hyphenCount++;
                    continue;
                }
            }
            if (token.charAt(i) == '.' || token.charAt(i) == ',' || token.charAt(i) == '!') {
                if (i != n - 1) {
                    return false;
                }
            }
        }
        return true;
    }
}
