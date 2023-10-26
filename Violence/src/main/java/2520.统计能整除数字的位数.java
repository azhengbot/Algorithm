/*
 * @lc app=leetcode.cn id=2520 lang=java
 *
 * [2520] 统计能整除数字的位数
 *
 * https://leetcode.cn/problems/count-the-digits-that-divide-a-number/description/
 *
 * algorithms
 * Easy (81.68%)
 * Likes:    18
 * Dislikes: 0
 * Total Accepted:    17.6K
 * Total Submissions: 20.7K
 * Testcase Example:  '7'
 *
 * 给你一个整数 num ，返回 num 中能整除 num 的数位的数目。
 * 
 * 如果满足 nums % val == 0 ，则认为整数 val 可以整除 nums 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：num = 7
 * 输出：1
 * 解释：7 被自己整除，因此答案是 1 。
 * 
 * 
 * 示例 2：
 * 
 * 输入：num = 121
 * 输出：2
 * 解释：121 可以被 1 整除，但无法被 2 整除。由于 1 出现两次，所以返回 2 。
 * 
 * 
 * 示例 3：
 * 
 * 输入：num = 1248
 * 输出：4
 * 解释：1248 可以被它每一位上的数字整除，因此答案是 4 。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= num <= 10^9
 * num 的数位中不含 0
 * 
 * 
 */

// @lc code=start
class Solution {
    public int countDigits(int num) {
        int ans = 0;
        int numBack = num;
        while (numBack != 0) {
            int i = numBack % 10;
            if (num % i == 0) {
                ans++;
            }
            numBack = numBack / 10;
        }
        return ans;
    }
}
// @lc code=end
