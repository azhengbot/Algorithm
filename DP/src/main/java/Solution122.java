public class Solution122 {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] opt = new int[n][2];

        opt[0][0] = 0;
        opt[0][1] = -prices[0];

        for (int i = 1; i < n; i++) {
            opt[i][0] = Math.max(opt[i - 1][0], opt[i - 1][1] + prices[i]);
            opt[i][1] = Math.max(opt[i - 1][1], opt[i - 1][0] - prices[i]);
        }

        return opt[n - 1][0];
    }
}
