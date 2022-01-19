public class Solution5 {
    public String longestPalindrome(String s) {
        int n = s.length();

        int maxLen = 1;
        int start = 0;

        // 最长为奇数
        for (int i = 0; i < n; i++) {
            int left = i - 1;
            int right = i + 1;
            // System.out.println(left + " " + right);
            while (left >= 0 && right < n && s.charAt(left) == s.charAt(right)) {
                left--;
                right++;
            }
            int len = right - left - 1;
            if (len > maxLen) {
                maxLen = len;
                start = left + 1;
            }
        }

        // 最长为偶数
        for (int i = 0; i < n; i++) {
            int left = i;
            int right = i + 1;

            while (left >= 0 && right < n && s.charAt(left) == s.charAt(right)) {
                left--;
                right++;
            }
            int len = right - left - 1;
            if (len > maxLen) {
                maxLen = len;
                start = left + 1;
            }
        }

        return s.substring(start, start + maxLen);
    }

    public static void main(String[] args) {
        Solution5 s = new Solution5();
        String res = s.longestPalindrome("babad");
        System.out.println(res);
    }
}
