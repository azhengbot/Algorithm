/*
 * @lc app=leetcode.cn id=200 lang=java
 *
 * [200] 岛屿数量
 *
 * https://leetcode-cn.com/problems/number-of-islands/description/
 *
 * algorithms
 * Medium (56.71%)
 * Likes:    1562
 * Dislikes: 0
 * Total Accepted:    403.9K
 * Total Submissions: 709.8K
 * Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
 *
 * 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
 * 
 * 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
 * 
 * 此外，你可以假设该网格的四条边均被水包围。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：grid = [
 * ⁠ ["1","1","1","1","0"],
 * ⁠ ["1","1","0","1","0"],
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["0","0","0","0","0"]
 * ]
 * 输出：1
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：grid = [
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["0","0","1","0","0"],
 * ⁠ ["0","0","0","1","1"]
 * ]
 * 输出：3
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * m == grid.length
 * n == grid[i].length
 * 1 
 * grid[i][j] 的值为 '0' 或 '1'
 * 
 * 
 */

// @lc code=start
import java.util.*;

class Solution200 {
    private boolean[][] used;
    private char[][] grid;
    private int m;
    private int n;

    public int numIslands(char[][] grid) {
        this.grid = grid;
        this.m = grid.length;
        this.n = grid[0].length;
        this.used = new boolean[m][n];

        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1' && !used[i][j]) {
                    // System.out.println(i + " " + j);
                    bfs(i, j);
                    ans++;
                }
            }
        }
        return ans;
    }

    private void bfs(int i, int j) {
        int[] di = new int[] { 1, 0, 0, -1 };
        int[] dj = new int[] { 0, 1, -1, 0 };
        ArrayDeque<int[]> dq = new ArrayDeque<>();
        // 第一步：push起点, 入队时将 used 标记
        dq.addLast(new int[] { i, j });
        used[i][j] = true;

        while (dq.size() != 0) {
            int[] land = dq.pollFirst();
            // 扩展所有出边（四个方向）
            for (int d = 0; d < 4; d++) {
                int ni = land[0] + di[d];
                int nj = land[1] + dj[d];
                // 任何时候访问数组前，判断合法性
                if (ni < 0 || nj < 0 || ni >= m || nj >= n) {
                    continue;
                }
                if (grid[ni][nj] == '1' && !used[ni][nj]) {
                    // BFS：入队时标记visit
                    dq.addLast(new int[] { ni, nj });
                    used[ni][nj] = true;
                }
            }
        }

    }
}
// @lc code=end
