package bfs;

import java.util.ArrayDeque;
import java.util.Queue;

public class Solution200 {
    private int m, n;
    private boolean[][] visited;
    private char[][] grid;

    public int numIslands(char[][] grid) {
        this.grid = grid;
        m = grid.length;
        n = grid[0].length;
        visited = new boolean[m][n];

        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    ans++;
                    bfs(i, j);
                }
            }
        }
        return ans;

    }

    private void bfs(int i, int j) {
        int[] dx = { 1, 0, 0, -1 };
        int[] dy = { 0, 1, -1, 0 };
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[] { i, j });
        visited[i][j] = true;

        System.out.println(q);
        while (!q.isEmpty()) {
            int x = q.peek()[0];
            int y = q.peek()[1];
            q.poll();
            for (int to = 0; to < 4; to++) {
                int ni = x + dx[to];
                int nj = y + dy[to];

                if (nj < 0 || ni < 0 || ni >= m || nj >= n)
                    continue;
                if (grid[ni][nj] == '0')
                    continue;
                if (visited[ni][nj])
                    continue;

                q.add(new int[] { ni, nj });
                visited[ni][nj] = true;
            }
        }

    }

    public static void main(String[] args) {

        Solution200 s = new Solution200();

        char[][] grid = {
                { '1', '1', '0', '0', '0' },
                { '1', '1', '0', '0', '0' },
                { '0', '0', '1', '0', '0' },
                { '0', '0', '0', '1', '1' },
        };

        int res = s.numIslands(grid);

        System.out.println(res);

        // Queue q = new ArrayDeque<>();
        // q.add(1);
        // q.add(2);
        // q.add(3);
        // System.out.println(q);
        // System.out.println(q.peek());
        // q.poll();
        // System.out.println(q);

    }

}
