public class Solution547 {
    int[] fa;

    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        fa = new int[n];

        for (int i = 0; i < n; i++) {
            fa[i] = i;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (isConnected[i][j] == 1) {
                    unionSet(i, j);
                }
            }
        }

        int ans = 0;

        for (int i = 0; i < n; i++) {
            if (fa[i] == i) {
                ans++;
            }
        }

        return ans;

    }

    private int find(int x) {
        if (x == fa[x]) {
            return x;
        }

        return fa[x] = find(fa[x]);
    }

    private void unionSet(int x, int y) {
        x = find(x);
        y = find(y);

        if (x != y) {
            fa[x] = y;
        }
    }
}
