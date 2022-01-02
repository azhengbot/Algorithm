package week07;

public class Solution279 {
    public int numSquares(int n) {
        int[] opt = new int[n + 1];

        for (int i = 1; i < n + 1; i++) {
            opt[i] = i;
            for (int j = 1; i - j * j >= 0; j++) {
                opt[i] = Math.min(opt[i], opt[i - j * j] + 1);
            }

        }
        return opt[n];
    }
}
