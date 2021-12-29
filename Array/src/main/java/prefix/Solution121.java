package prefix;

public class Solution121 {
    public int maxProfit(int[] prices) {
        int n = prices.length;

        int[] pre_min = new int[n];
        pre_min[0] = prices[0];

        for (int i = 1; i < n; i++) {
            pre_min[i] = Math.min(pre_min[i - 1], prices[i]);
        }

        int ans = 0;

        for (int i = 0; i < n; i++) {
            ans = Math.max(ans, prices[i] - pre_min[i]);
        }

        return ans;
    }

}
