/*
 * @lc app=leetcode.cn id=2609 lang=java
 *
 * [2609] 最长平衡子字符串
 *
 * https://leetcode.cn/problems/find-the-longest-balanced-substring-of-a-binary-string/description/
 *
 * algorithms
 * Easy (49.31%)
 * Likes:    39
 * Dislikes: 0
 * Total Accepted:    15.6K
 * Total Submissions: 28.3K
 * Testcase Example:  '"01000111"'
 *
 * 给你一个仅由 0 和 1 组成的二进制字符串 s 。  
 * 
 * 如果子字符串中 所有的 0 都在 1 之前 且其中 0 的数量等于 1 的数量，则认为 s
 * 的这个子字符串是平衡子字符串。请注意，空子字符串也视作平衡子字符串。 
 * 
 * 返回  s 中最长的平衡子字符串长度。
 * 
 * 子字符串是字符串中的一个连续字符序列。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：s = "01000111"
 * 输出：6
 * 解释：最长的平衡子字符串是 "000111" ，长度为 6 。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：s = "00111"
 * 输出：4
 * 解释：最长的平衡子字符串是 "0011" ，长度为  4 。
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：s = "111"
 * 输出：0
 * 解释：除了空子字符串之外不存在其他平衡子字符串，所以答案为 0 。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s.length <= 50
 * '0' <= s[i] <= '1'
 * 
 * 
 */

// @lc code=start
class Solution {
    public int findTheLongestBalancedSubstring(String s) {
        int n = s.length();
        int ans = 0;
        if (s.length() == 0) {
            return 0;
        }

        for (int i = 1; i < n; i++) {
            if (s.charAt(i) == '1' && s.charAt(i - 1) == '0') {
                int left = 0;
                int right = 0;
                for (int j = i - 1; j >= 0; j--) {
                    if (s.charAt(j) == '1') {
                        break;
                    }
                    left++;
                }
                for (int k = i; k < n; k++) {
                    if (s.charAt(k) == '0') {
                        break;
                    }
                    right++;
                }
                ans = Math.max(ans, Math.min(left, right));

            }
        }
        return ans * 2;

    }
}
// @lc code=end
