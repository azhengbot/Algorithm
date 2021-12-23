
// https://leetcode-cn.com/problems/coin-change/
import java.util.*;

public class Solution322 {
    public int coinChange(int[] coins, int amount) {
        int[] opt = new int[amount + 1];
        Arrays.fill(opt, amount + 1);
        opt[0] = 0;
        for (int i = 1; i < amount + 1; i++) {
            for (int coin : coins) {
                if (i - coin < 0) {
                    continue;
                }

                opt[i] = Math.min(opt[i], opt[i - coin] + 1);

            }

        }

        return opt[amount] == amount + 1 ? -1 : opt[amount];
    }
}
