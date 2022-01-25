public class Solution50 {
    public double myPow(double x, int n) {
        if (n == Integer.MIN_VALUE) {
            return 1.0 / (myPow(x, -(n + 1)) * x);
        }

        if (n == 0) {
            return 1.0;
        }

        if (n < 0) {
            return 1.0 / myPow(x, -n);
        }

        double ans = 1.0;
        double temp = x;

        while (n > 0) {
            if ((n & 1) == 1) {
                ans = ans * temp;
            }
            temp = temp * temp;
            n = n >> 1;
        }

        return ans;
    }
}
