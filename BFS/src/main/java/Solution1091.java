/*
 * @lc app=leetcode.cn id=1091 lang=java
 *
 * [1091] 二进制矩阵中的最短路径
 *
 * https://leetcode.cn/problems/shortest-path-in-binary-matrix/description/
 *
 * algorithms
 * Medium (38.73%)
 * Likes:    288
 * Dislikes: 0
 * Total Accepted:    66.7K
 * Total Submissions: 169.3K
 * Testcase Example:  '[[0,1],[1,0]]'
 *
 * 给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。
 * 
 * 二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n -
 * 1)）的路径，该路径同时满足下述要求：
 * 
 * 
 * 路径途经的所有单元格都的值都是 0 。
 * 路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
 * 
 * 
 * 畅通路径的长度 是该路径途经的单元格总数。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：grid = [[0,1],[1,0]]
 * 输出：2
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：grid = [[0,0,0],[1,1,0],[1,1,0]]
 * 输出：4
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：grid = [[1,0,0],[1,1,0],[1,1,0]]
 * 输出：-1
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * n == grid.length
 * n == grid[i].length
 * 1 
 * grid[i][j] 为 0 或 1
 * 
 * 
 */

// @lc code=start

import java.util.*;

public class Solution1091 {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        int[] x = { 0, 0, 1, -1, 1, 1, -1, -1 };
        int[] y = { 1, -1, 0, 0, 1, -1, 1, -1 };
        boolean[][] used = new boolean[n][n];

        ArrayDeque<Integer[]> dq = new ArrayDeque<>();
        dq.add(new Integer[] { 0, 0 });
        used[0][0] = true;
        int cnt = 1;
        if (grid[0][0] == 1) {
            return -1;
        }
        while (dq.size() != 0) {
            ArrayDeque<Integer[]> dqCopy = new ArrayDeque<>();

            for (Integer[] coord : dq) {
                Integer i = coord[0];
                Integer j = coord[1];
                if (i == n - 1 && j == n - 1) {
                    return cnt;
                }
                for (int k = 0; k < 8; k++) {
                    Integer ni = i + x[k];
                    Integer nj = j + y[k];
                    if (ni < 0 || nj < 0 || ni >= n || nj >= n || grid[ni][nj] == 1)
                        continue;
                    if (used[ni][nj])
                        continue;
                    dqCopy.add(new Integer[] { ni, nj });
                    used[ni][nj] = true;
                }
            }
            dq = dqCopy;
            cnt++;
        }
        return -1;

    }

    public static void main(String[] args) {
        Solution1091 s = new Solution1091();
        int[][] grid = { { 1, 2 }, { 3, 4 }, { 5, 6 } };
        int res = s.shortestPathBinaryMatrix(grid);
        System.out.println(res);
    }
}

// @lc code=end
