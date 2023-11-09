
/*
 * @lc app=leetcode.cn id=2258 lang=java
 *
 * [2258] 逃离火灾
 *
 * https://leetcode.cn/problems/escape-the-spreading-fire/description/
 *
 * algorithms
 * Hard (36.79%)
 * Likes:    82
 * Dislikes: 0
 * Total Accepted:    6.5K
 * Total Submissions: 13.7K
 * Testcase Example:  '[[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]'
 *
 * 给你一个下标从 0 开始大小为 m x n 的二维整数数组 grid ，它表示一个网格图。每个格子为下面 3 个值之一：
 * 
 * 
 * 0 表示草地。
 * 1 表示着火的格子。
 * 2 表示一座墙，你跟火都不能通过这个格子。
 * 
 * 
 * 一开始你在最左上角的格子 (0, 0) ，你想要到达最右下角的安全屋格子 (m - 1, n - 1) 。每一分钟，你可以移动到 相邻
 * 的草地格子。每次你移动 之后 ，着火的格子会扩散到所有不是墙的 相邻 格子。
 * 
 * 请你返回你在初始位置可以停留的 最多 分钟数，且停留完这段时间后你还能安全到达安全屋。如果无法实现，请你返回 -1 。如果不管你在初始位置停留多久，你
 * 总是 能到达安全屋，请你返回 10^9 。
 * 
 * 注意，如果你到达安全屋后，火马上到了安全屋，这视为你能够安全到达安全屋。
 * 
 * 如果两个格子有共同边，那么它们为 相邻 格子。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 输入：grid =
 * [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]
 * 输出：3
 * 解释：上图展示了你在初始位置停留 3 分钟后的情形。
 * 你仍然可以安全到达安全屋。
 * 停留超过 3 分钟会让你无法安全到达安全屋。
 * 
 * 示例 2：
 * 
 * 
 * 
 * 输入：grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]
 * 输出：-1
 * 解释：上图展示了你马上开始朝安全屋移动的情形。
 * 火会蔓延到你可以移动的所有格子，所以无法安全到达安全屋。
 * 所以返回 -1 。
 * 
 * 
 * 示例 3：
 * 
 * 
 * 
 * 输入：grid = [[0,0,0],[2,2,0],[1,2,0]]
 * 输出：1000000000
 * 解释：上图展示了初始网格图。
 * 注意，由于火被墙围了起来，所以无论如何你都能安全到达安全屋。
 * 所以返回 10^9 。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * m == grid.length
 * n == grid[i].length
 * 2 <= m, n <= 300
 * 4 <= m * n <= 2 * 10^4
 * grid[i][j] 是 0 ，1 或者 2 。
 * grid[0][0] == grid[m - 1][n - 1] == 0
 * 
 * 
 */
import java.lang.reflect.Array;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Queue;

// @lc code=start
class Solution {

    ArrayDeque<Integer[]> qFire = new ArrayDeque<>();
    ArrayDeque<Integer[]> qPerson = new ArrayDeque<>();
    int[] dx = new int[] { 1, -1, 0, 0 };
    int[] dy = new int[] { 0, 0, 1, -1 };
    int[][] grid;
    int m;
    int n;
    boolean[][] fired;
    boolean[][] personed;

    private void spreadFire() {
        ArrayDeque<Integer[]> tmp = qFire;
        qFire = new ArrayDeque<>();

        for (Integer[] curFire : tmp) {
            int firex = curFire[0];
            int firey = curFire[1];

            for (int d = 0; d < 4; d++) {
                int x = dx[d];
                int y = dy[d];
                int nfx = firex + x;
                int nfy = firey + y;

                if (nfx >= 0 && nfy >= 0 && nfx < m && nfy < n && !fired[nfx][nfy] && grid[nfx][nfy] == 0) {
                    fired[nfx][nfy] = true;
                    qFire.add(new Integer[] { nfx, nfy });
                }
            }
        }
    }

    private boolean check(int mid) {

        qFire = new ArrayDeque<>();
        fired = new boolean[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    fired[i][j] = true;
                    qFire.add(new Integer[] { i, j });
                }
            }
        }
        while (mid-- > 0 && !qFire.isEmpty()) {
            spreadFire();
        }
        if (fired[0][0]) {
            return false;
        }

        qPerson = new ArrayDeque<>();
        qPerson.add(new Integer[] { 0, 0 });
        personed = new boolean[m][n];
        personed[0][0] = true;

        while (!qPerson.isEmpty()) {
            ArrayDeque<Integer[]> tmp = qPerson;
            qPerson = new ArrayDeque<>();
            for (Integer[] curPerson : tmp) {
                // Integer[] curPerson = qPerson.pollFirst();
                int px = curPerson[0];
                int py = curPerson[1];

                if (fired[px][py]) {
                    continue;
                }

                for (int pd = 0; pd < 4; pd++) {
                    int npx = px + dx[pd];
                    int npy = py + dy[pd];

                    if (npx >= 0 && npy >= 0 && npx < m && npy < n
                            && !fired[npx][npy] && !personed[npx][npy] && grid[npx][npy] == 0) {
                        if (npx == m - 1 && npy == n - 1) {
                            return true;
                        }
                        personed[npx][npy] = true;
                        qPerson.add(new Integer[] { npx, npy });

                    }
                }
            }
            spreadFire();

        }
        return false;
    }

    public int maximumMinutes(int[][] grid) {
        int ans = (int) Math.pow(10, 9);
        m = grid.length;
        n = grid[0].length;
        this.grid = grid;

        int l = -1;
        int r = m * n + 1;

        while (l + 1 < r) {
            int mid = (l + r) >>> 1;
            if (check(mid)) {
                l = mid;
            } else {
                r = mid;
            }
        }

        return l < m * n ? l : ans;
    }
}

// @lc code=end
