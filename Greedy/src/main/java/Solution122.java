// https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
public class Solution122 {

    public int maxProfit(int[] prices) {
        int n = prices.length;

        int ans = 0;
        for (int i = 1; i < n; i++) {
            ans = Math.max(prices[i] - prices[i - 1], 0) + ans;
        }

        return ans;
    }

}
