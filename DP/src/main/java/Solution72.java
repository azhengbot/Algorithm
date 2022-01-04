public class Solution72 {
    public int minDistance(String word1, String word2) {
        word1 = " " + word1;
        word2 = " " + word2;

        int m = word1.length();
        int n = word2.length();

        int[][] opt = new int[m][n];

        for (int i = 0; i < m; i++) {
            opt[i][0] = i;
        }
        for (int j = 0; j < n; j++) {
            opt[0][j] = j;
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                int temp = Math.min(opt[i - 1][j] + 1, opt[i][j - 1] + 1);
                if (word1.charAt(i) == word2.charAt(j)) {
                    opt[i][j] = Math.min(temp, opt[i - 1][j - 1]);
                } else {
                    opt[i][j] = Math.min(temp, opt[i - 1][j - 1] + 1);
                }

            }
        }

        return opt[m - 1][n - 1];
    }
}
