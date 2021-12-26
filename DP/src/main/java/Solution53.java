public class Solution53 {
    public int maxSubArray(int[] nums) {
        int n = nums.length;

        int[] opt = new int[n];
        opt[0] = nums[0];

        for (int i = 1; i < n; i++) {
            opt[i] = Math.max(opt[i - 1] + nums[i], nums[i]);
        }

        int ans = nums[0];

        for (int o : opt) {
            ans = Math.max(ans, o);
        }

        return ans;

    }
}
