/*
 * @lc app=leetcode.cn id=522 lang=java
 *
 * [522] 最长特殊序列 II
 *
 * https://leetcode.cn/problems/longest-uncommon-subsequence-ii/description/
 *
 * algorithms
 * Medium (48.86%)
 * Likes:    226
 * Dislikes: 0
 * Total Accepted:    44.5K
 * Total Submissions: 87.9K
 * Testcase Example:  '["aba","cdc","eae"]'
 *
 * 给定字符串列表 strs ，返回其中 最长的特殊序列 的长度。如果最长特殊序列不存在，返回 -1 。
 * 
 * 特殊序列 定义如下：该序列为某字符串 独有的子序列（即不能是其他字符串的子序列）。
 * 
 * s 的 子序列可以通过删去字符串 s 中的某些字符实现。
 * 
 * 
 * 例如，"abc" 是 "aebdc" 的子序列，因为您可以删除"aebdc"中的下划线字符来得到 "abc"
 * 。"aebdc"的子序列还包括"aebdc"、 "aeb" 和 "" (空字符串)。
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入: strs = ["aba","cdc","eae"]
 * 输出: 3
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: strs = ["aaa","aaa","aa"]
 * 输出: -1
 * 
 * 
 * 
 * 
 * 提示:
 * 
 * 
 * 2 <= strs.length <= 50
 * 1 <= strs[i].length <= 10
 * strs[i] 只包含小写英文字母
 * 
 * 
 */

// @lc code=start
class Solution {
    private boolean check(String s1, String s2) {
        int m = s1.length();
        int n = s2.length();
        int i = 0;

        for (int j = 0; j < n; j++) {
            Character c2 = s2.charAt(j);
            if (c2 == s1.charAt(i)) {
                i += 1;
                if (i == m) {
                    return true;
                }
            }

        }
        return false;
    }

    public int findLUSlength(String[] strs) {
        int ans = -1;
        int l = strs.length;
        boolean flag = false;
        for (int i = 0; i < l; i++) {
            for (int j = 0; j < l; j++) {
                // System.out.println(check(strs[i], strs[j]) + "...." + strs[j] + "...." + strs[i]);
                if (i != j && check(strs[i], strs[j])) {
                    flag = true;
                    break;
                }
            }
            if (!flag && strs[i].length() > ans) {
                ans = strs[i].length();
            }
            flag = false;

        }
        return ans;
    }
}
// @lc code=end
