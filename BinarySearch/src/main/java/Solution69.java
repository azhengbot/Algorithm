public class Solution69 {
    public int mySqrt(int x) {
        int left = 0;
        int right = x;
        while (left < right) {
            int mid = (left + right + 1) / 2;
            if (mid * mid <= x) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return right;
    }

    public static void main(String[] args) {
        Solution69 s = new Solution69();
        int x = 8;
        int res = s.mySqrt(x);
        System.out.println(res);
    }

}
