
public class Solution45 {
    public int jump(int[] nums) {
        int now = 0;
        int ans = 0;

        while (now < nums.length - 1) {
            int right = now + nums[now];

            if (right >= nums.length - 1) {
                ans++;
                return ans;
            }

            int nextRight = right;
            int next = now;
            for (int i = now + 1; i <= right; i++) {
                if (i + nums[i] > nextRight) {
                    nextRight = i + nums[i];
                    next = i;
                }
            }
            now = next;
            ans++;

        }
        return ans;

    }
}
