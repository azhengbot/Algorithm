package complete_backpack;

public class solution518 {
    public int change(int amount, int[] coins) {
        int n = coins.length;
        int[][] opt = new int[n + 1][amount + 1];

        opt[0][0] = 1;

        for (int i = 1; i < n + 1; i++) {
            int val = coins[i - 1];

            for (int j = 0; j < amount + 1; j++) {
                opt[i][j] = opt[i - 1][j];

                for (int k = 1; k * val <= j; j++) {
                    opt[i][j] = opt[i - 1][j - k * val] + opt[i][j];
                }
            }

        }

        return opt[n][amount];

    }

}
