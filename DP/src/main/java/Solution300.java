import java.util.*;

public class Solution300 {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[] opt = new int[n];

        Arrays.fill(opt, 1);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j])
                    opt[i] = Math.max(opt[i], opt[j] + 1);
            }

        }

        int ans = 0;

        for (int o : opt) {
            ans = Math.max(ans, o);
        }

        return ans;
    }
}
