package monotonicity;

//https://leetcode-cn.com/problems/plus-one/submissions/
public class Solution66 {
    public int[] plusOne(int[] digits) {
        int len = digits.length;
        for (int i = len - 1; i >= 0; i--) {

            if (digits[i] != 9) {
                digits[i]++;
                for (int j = i + 1; j < len; j++) {
                    digits[j] = 0;
                }
                return digits;
            }
        }
        int[] ans = new int[len + 1];
        ans[0] = 1;
        return ans;

    }
}
