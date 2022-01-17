public class Solution680 {
    public boolean validPalindrome(String s) {

        return check(s, 1);

    }

    private boolean check(String s, int times) {
        System.out.println(s);
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            // System.out.println(left + " " + right);
            if (s.charAt(left) != s.charAt(right)) {
                if (times > 0) {
                    return check(s.substring(left, right), 0) || check(s.substring(left + 1, right + 1), 0);
                }
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public static void main(String[] args) {
        Solution680 s = new Solution680();
        s.validPalindrome("abc");
        System.out.println(s.validPalindrome("abc"));
    }
}
