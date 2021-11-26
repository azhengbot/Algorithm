// https://leetcode-cn.com/problems/maximum-subarray/

public class Solution53 {
    public int maxSubArray(int[] nums) {
        int len = nums.length;
        int[] preSum = new int[len + 1];

        for (int i = 1; i <= len; i++) {
            preSum[i] = preSum[i - 1] + nums[i - 1];
        }

        int maxRes = nums[0];

        // 这个超时了
        // for (int i = 0; i <= len; i++) {
        // for (int j = 0; j < i; j++) {
        // int res = preSum[i] - preSum[j];
        // if (res > maxRes) {
        // maxRes = res;
        // }
        // }
        // }

        int[] preMin = new int[len + 1];
        preMin[0] = preSum[0];
        for (int i = 1; i < len + 1; i++) {
            preMin[i] = Math.min(preSum[i], preMin[i - 1]);
        }

        for (int i = 1; i < len + 1; i++) {
            maxRes = Math.max(maxRes, preSum[i] - preMin[i - 1]);
        }

        return maxRes;
    }

    public static void main(String[] args) {
        // int[] nums = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
        int[] nums = { 5, 4, -1, 7, 8 };
        // int[] nums = { -1 };

        Solution53 s = new Solution53();
        int res = s.maxSubArray(nums);
        System.out.println(res);
    }

}