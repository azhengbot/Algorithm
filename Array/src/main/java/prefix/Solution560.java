package prefix;

import java.util.HashMap;

public class Solution560 {
    public int subarraySum(int[] nums, int k) {
        int[] preSums = new int[nums.length + 1];

        for (int i = 1; i < nums.length + 1; i++) {
            preSums[i] = preSums[i - 1] + nums[i - 1];
        }

        HashMap<Integer, Integer> cntMap = new HashMap<>();
        int ans = 0;

        for (int preSum : preSums) {
            if (cntMap.containsKey(preSum - k)) {
                ans = ans + cntMap.get(preSum - k);
            }

            int cnt = cntMap.getOrDefault(preSum, 0);
            ++cnt;
            cntMap.put(preSum, cnt);
        }

        return ans;

    }

    public static void main(String[] args) {
        Solution560 s = new Solution560();
        int[] nums = { 1, -1, 0 };
        int k = 0;

        int res = s.subarraySum(nums, k);

        System.out.println(res);
    }
}
