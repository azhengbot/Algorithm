public class Solution8 {
    public int myAtoi(String s) {
        boolean isPre = true;
        int res = 0;
        int sign = 1;

        for (char ch : s.toCharArray()) {
            if (isPre && !checkNum(ch) && ch != '+' && ch != '-' && ch != ' ') {
                return 0;
            }

            if (!isPre && !checkNum(ch)) {
                return res * sign;
            }

            if (ch == '+' && isPre) {
                sign = 1;
                isPre = false;
            }

            if (ch == '-' && isPre) {
                sign = -1;
                isPre = false;
            }

            if (checkNum(ch)) {
                isPre = false;
                if ((res * 10L + (ch - '0')) * sign > (long) Integer.MAX_VALUE) {
                    return Integer.MAX_VALUE;
                } else if ((res * 10L + (ch - '0')) * sign < (long) Integer.MIN_VALUE) {
                    return Integer.MIN_VALUE;
                }

                res = res * 10 + (ch - '0');

            }

        }
        return res * sign;
    }

    private boolean checkNum(char ch) {
        if (ch >= '0' && ch <= '9') {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {

    }
}