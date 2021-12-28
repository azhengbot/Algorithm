public class Solution152 {
    public int maxProduct(int[] nums) {
        int n = nums.length;

        int[] optMax = new int[n];
        int[] optMin = new int[n];
        optMax[0] = nums[0];
        optMin[0] = nums[0];

        for (int i = 1; i < n; i++) {
            optMax[i] = Math.max(Math.max(optMax[i - 1] * nums[i], optMin[i - 1] * nums[i]), nums[i]);

            optMin[i] = Math.min(Math.min(optMax[i - 1] * nums[i], optMin[i - 1] * nums[i]), nums[i]);
        }

        int ans = nums[0];

        for (int i = 0; i < n; i++) {
            ans = Math.max(ans, optMax[i]);
        }

        return ans;

    }
}
