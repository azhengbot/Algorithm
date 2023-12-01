/*
 * @lc app=leetcode.cn id=2661 lang=java
 *
 * [2661] 找出叠涂元素
 *
 * https://leetcode.cn/problems/first-completely-painted-row-or-column/description/
 *
 * algorithms
 * Medium (51.67%)
 * Likes:    48
 * Dislikes: 0
 * Total Accepted:    16.6K
 * Total Submissions: 28K
 * Testcase Example:  '[1,3,4,2]\n[[1,4],[2,3]]'
 *
 * 给你一个下标从 0 开始的整数数组 arr 和一个 m x n 的整数 矩阵 mat 。arr 和 mat 都包含范围 [1，m * n] 内的 所有
 * 整数。
 * 
 * 从下标 0 开始遍历 arr 中的每个下标 i ，并将包含整数 arr[i] 的 mat 单元格涂色。
 * 
 * 请你找出 arr 中在 mat 的某一行或某一列上都被涂色且下标最小的元素，并返回其下标 i 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：arr = [1,3,4,2], mat = [[1,4],[2,3]]
 * 输出：2
 * 解释：遍历如上图所示，arr[2] 在矩阵中的第一行或第二列上都被涂色。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
 * 输出：3
 * 解释：遍历如上图所示，arr[3] 在矩阵中的第二列上都被涂色。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * m == mat.length
 * n = mat[i].length
 * arr.length == m * n
 * 1 <= m, n <= 10^5
 * 1 <= m * n <= 10^5
 * 1 <= arr[i], mat[r][c] <= m * n
 * arr 中的所有整数 互不相同
 * mat 中的所有整数 互不相同
 * 
 * 
 */

// @lc code=start

import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public int firstCompleteIndex(int[] arr, int[][] mat) {
        int rowCnt = mat.length;
        int colCnt = mat[0].length;
        int n = arr.length;
        int[] row = new int[rowCnt];
        int[] col = new int[colCnt];

        HashMap<Integer, Integer[]> arrMap = new HashMap<>();

        for (int i = 0; i < rowCnt; i++) {
            for (int j = 0; j < colCnt; j++) {
                arrMap.put(mat[i][j], new Integer[] { i, j });
            }
        }

        // System.out.println(arrMap);

        for (int k = 0; k < n; k++) {
            Integer[] pos = arrMap.get(arr[k]);
            Integer i = pos[0];
            Integer j = pos[1];

            row[i]++;
            col[j]++;

            // System.out.println(Arrays.toString(row));
            // System.out.println(Arrays.toString(col));
            if (row[i] >= colCnt) {
                return k;
            }

            if (col[j] >= rowCnt) {
                return k;
            }
        }

        return 0;

    }
}
// @lc code=end

// [[4,3,5],
// [1,2,6]]
