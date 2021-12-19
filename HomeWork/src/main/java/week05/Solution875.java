package week05;

public class Solution875 {
    int[] piles;
    int h;

    public int minEatingSpeed(int[] piles, int h) {
        this.piles = piles;
        this.h = h;

        long left = 0;
        long right = 0;
        for (int pile : piles) {
            right += pile;
        }

        while (left < right) {
            long mid = (left + right) / 2;

            if (check(mid)) {
                right = mid;
            } else {
                left = mid + 1L;
            }
        }
        return (int) right;

    }

    private boolean check(long k) {
        int use_hour = 0;

        for (int pile : piles) {
            if (k == 0)
                return false;
            long need_hour = (long) Math.ceil((double) pile / (double) k);
            use_hour += need_hour;

            if (use_hour > h)
                return false;

        }
        return use_hour <= h;
    }
}
