package week08;

import java.util.HashSet;

public class Solution200 {
    private int[] fa;

    public int numIslands(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        fa = new int[m * n];

        for (int i = 0; i < m * n; i++) {
            fa[i] = i;
        }

        int[] dx = new int[] { 1, 0, 0, -1 };
        int[] dy = new int[] { 0, 1, -1, 0 };

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '0')
                    continue;
                for (int k = 0; k < 4; k++) {
                    int ni = i + dx[k];
                    int nj = j + dy[k];

                    if (ni < 0 || nj < 0 || ni >= m || nj >= n) {
                        continue;
                    }
                    if (grid[ni][nj] == '0') {
                        continue;
                    }
                    unionSet(i * n + j, ni * n + nj);
                }
            }
        }

        HashSet<Integer> ans = new HashSet<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    ans.add(find(i * n + j));
                }
            }
        }

        return ans.size();
    }

    private int find(int x) {
        if (x == fa[x])
            return x;

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