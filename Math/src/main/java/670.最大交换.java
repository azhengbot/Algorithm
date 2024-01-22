/*
 * @lc app=leetcode.cn id=670 lang=java
 *
 * [670] 最大交换
 *
 * https://leetcode.cn/problems/maximum-swap/description/
 *
 * algorithms
 * Medium (48.02%)
 * Likes:    440
 * Dislikes: 0
 * Total Accepted:    77.2K
 * Total Submissions: 158.9K
 * Testcase Example:  '2736'
 *
 * 给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
 * 
 * 示例 1 :
 * 
 * 
 * 输入: 2736
 * 输出: 7236
 * 解释: 交换数字2和数字7。
 * 
 * 
 * 示例 2 :
 * 
 * 
 * 输入: 9973
 * 输出: 9973
 * 解释: 不需要交换。
 * 
 * 
 * 注意:
 * 
 * 
 * 给定数字的范围是 [0, 10^8]
 * 
 * 
 */

6578941 9999941

// @lc code=start

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

class Solution {
    public int maximumSwap(int num) {
        int back = num;
        Deque dq = new ArrayDeque<>();
        int n = 0;
        int max = 0;
        int left = 0;
        int leftV = -1;
        int right = 0;
        int rightV = -1;

        int curRight = 0;
        int curRightV = -1;
        while (num > 0) {
            int v = num % 10;
            if (v > max) {
                max = v;
                right = n;
                rightV = v;
            }
            if (v < max) {
                left = n;
                leftV = v;
                curRight = right;
                curRightV = rightV;

            }
            n++;
            num = num / 10;
        }

        if (left == 0 && leftV == -1) {
            return back;
        }

        // System.out.println(n - left -1);
        // System.out.println(leftV);
        // System.out.println(n - right -1);
        // System.out.println(rightV);
        // int l = n - left -1;
        // int r = n -right -1;

        int res = back - 
         leftV * (int) Math.pow(10, left) +  leftV * (int) Math.pow(10, curRight) -  curRightV * (int) Math.pow(10, curRight) +  curRightV * (int) Math.pow(10, left);

        return res;
        
    }
}
// @lc code=end
