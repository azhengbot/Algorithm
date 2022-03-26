
// @lc code=start
class Solution1248 {
    public int numberOfSubarrays(int[] nums, int k) {

        int n = nums.length;
        int[] preSum = new int[n + 1];
        int ans = 0;
        int[] count = new int[n + 1];

        for (int i = 1; i < n + 1; i++) {
            preSum[i] = preSum[i - 1] + nums[i - 1] % 2;
        }
        // preSum[r] - preSum[l] = k
        // preSum[r] - k = preSum[l]
        for (int i = 0; i < n + 1; i++) {
            if (preSum[i] - k >= 0) {
                ans += count[preSum[i] - k];
            }
            count[preSum[i]] += 1;
        }
        return ans;
    }
}
// @lc code=end
