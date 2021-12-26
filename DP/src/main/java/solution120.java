import java.util.List;

public class solution120 {

    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        // 倒着想
        int[][] opt = new int[n][n];
        opt[0][0] = triangle.get(0).get(0);

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i + 1; j++) {
                if (j == 0) {
                    opt[i][j] = triangle.get(i).get(j) + opt[i - 1][0];
                } else if (j == i) {
                    opt[i][j] = triangle.get(i).get(j) + opt[i - 1][j - 1];
                } else {
                    opt[i][j] = triangle.get(i).get(j) + Math.min(opt[i - 1][j], opt[i - 1][j - 1]);
                }
            }
        }

        int ans = opt[n - 1][0];

        for (int i : opt[n - 1]) {
            ans = Math.min(i, ans);
        }

        return ans;
    }

}
