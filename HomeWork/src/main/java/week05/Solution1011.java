package week05;

public class Solution1011 {
    int[] weights;
    int days;

    public int shipWithinDays(int[] weights, int days) {
        this.weights = weights;
        this.days = days;

        int left = 0;
        int right = 0;

        for (int weight : weights) {
            right += weight;

            if (weight > left) {
                left = weight;
            }
        }

        while (left < right) {
            int mid = (left + right) / 2;

            if (check(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return right;
    }

    private boolean check(int box) {
        int useDay = 0;
        int hasWeight = 0;
        for (int weight : weights) {
            hasWeight += weight;
            if (hasWeight > box) {
                useDay += 1;
                if (useDay > days) {
                    return false;
                }
                hasWeight = weight;
            }
        }
        return useDay < days;

    }

    public static void main(String[] args) {
        Solution1011 s = new Solution1011();
        int[] weights = { 1, 2, 3, 1, 1 };
        int days = 4;

        int res = s.shipWithinDays(weights, days);
        System.out.println(res);
    }

}
