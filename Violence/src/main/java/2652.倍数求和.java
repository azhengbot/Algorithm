/*
 * @lc app=leetcode.cn id=2652 lang=java
 *
 * [2652] 倍数求和
 *
 * https://leetcode.cn/problems/sum-multiples/description/
 *
 * algorithms
 * Easy (79.07%)
 * Likes:    31
 * Dislikes: 0
 * Total Accepted:    15.7K
 * Total Submissions: 19.5K
 * Testcase Example:  '7'
 *
 * 给你一个正整数 n ，请你计算在 [1，n] 范围内能被 3、5、7 整除的所有整数之和。
 * 
 * 返回一个整数，用于表示给定范围内所有满足约束条件的数字之和。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：n = 7
 * 输出：21
 * 解释：在 [1, 7] 范围内能被 3、5、7 整除的所有整数分别是 3、5、6、7 。数字之和为 21 。
 * 
 * 
 * 示例 2：
 * 
 * 输入：n = 10
 * 输出：40
 * 解释：在 [1, 10] 范围内能被 3、5、7 整除的所有整数分别是 3、5、6、7、9、10 。数字之和为 40 。
 * 
 * 
 * 示例 3：
 * 
 * 输入：n = 9
 * 输出：30
 * 解释：在 [1, 9] 范围内能被 3、5、7 整除的所有整数分别是 3、5、6、7、9 。数字之和为 30 。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= n <= 10^3
 * 
 * 
 */

// @lc code=start
class Solution {
    public int sumOfMultiples(int n) {
        int[] nu = new int[] { 3, 5, 7 };
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < 3; j++) {
                if (i % nu[j] == 0) {
                    ans += i;
                    break;
                }
            }
        }
        return ans;

    }
}
// @lc code=end
