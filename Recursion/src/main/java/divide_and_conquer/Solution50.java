package divide_and_conquer;

public class Solution50 {
    public double myPow(double x, int n) {
        if (n == Integer.MIN_VALUE) {
            return 1 / (myPow(x, -(n + 1)) * x);
        }

        if (n < 0) {
            return 1 / (myPow(x, -n));
        }

        if (n == 0) {
            return 1;
        }

        double temp = myPow(x, n / 2);

        double ans = temp * temp;

        if (n % 2 != 0) {
            ans = ans * x;
        }

        return ans;
    }

    public static void main(String[] args) {

        Solution50 s = new Solution50();
        System.out.println(s.myPow(2, 10));
        System.out.println(s.myPow(2, -2));

    }
}
