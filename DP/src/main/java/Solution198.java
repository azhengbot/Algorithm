public class Solution198 {
    public int rob(int[] nums) {
        int n = nums.length;
        int[][] opt = new int[n][2];

        opt[0][0] = 0;
        opt[0][1] = nums[0];

        for (int i = 1; i < n; i++) {
            opt[i][0] = Math.max(opt[i - 1][0], opt[i - 1][1]);
            opt[i][1] = opt[i - 1][0] + nums[i];
        }

        return Math.max(opt[n - 1][0], opt[n - 1][1]);
    }
}
