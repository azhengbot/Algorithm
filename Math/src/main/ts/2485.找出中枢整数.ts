/*
 * @lc app=leetcode.cn id=2485 lang=typescript
 *
 * [2485] 找出中枢整数
 *
 * https://leetcode.cn/problems/find-the-pivot-integer/description/
 *
 * algorithms
 * Easy (80.31%)
 * Likes:    39
 * Dislikes: 0
 * Total Accepted:    20.4K
 * Total Submissions: 24.9K
 * Testcase Example:  '8'
 *
 * 给你一个正整数 n ，找出满足下述条件的 中枢整数 x ：
 * 
 * 
 * 1 和 x 之间的所有元素之和等于 x 和 n 之间所有元素之和。
 * 
 * 
 * 返回中枢整数 x 。如果不存在中枢整数，则返回 -1 。题目保证对于给定的输入，至多存在一个中枢整数。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：n = 8
 * 输出：6
 * 解释：6 是中枢整数，因为 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21 。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：n = 1
 * 输出：1
 * 解释：1 是中枢整数，因为 1 = 1 。
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：n = 4
 * 输出：-1
 * 解释：可以证明不存在满足题目要求的整数。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= n <= 1000
 * 
 * 
 */

// @lc code=start
function pivotInteger(n: number): number {
    let sum = 0;
    for (let index = 1; index < n + 1; index++) {
        sum += index;
    }
    let preSum = 0;
    for (let i = 1; i < n + 1; i++) {
        if (preSum == sum - preSum - i) {
            return i;
        }
        preSum += i;
    }
    return -1;

};
// @lc code=end

