/*
 * @lc app=leetcode.cn id=318 lang=java
 *
 * [318] 最大单词长度乘积
 *
 * https://leetcode.cn/problems/maximum-product-of-word-lengths/description/
 *
 * algorithms
 * Medium (72.46%)
 * Likes:    478
 * Dislikes: 0
 * Total Accepted:    83K
 * Total Submissions: 114.6K
 * Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
 *
 * 给你一个字符串数组 words ，找出并返回 length(words[i]) * length(words[j])
 * 的最大值，并且这两个单词不含有公共字母。如果不存在这样的两个单词，返回 0 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：words = ["abcw","baz","foo","bar","xtfn","abcdef"]
 * 输出：16 
 * 解释：这两个单词为 "abcw", "xtfn"。
 * 
 * 示例 2：
 * 
 * 
 * 输入：words = ["a","ab","abc","d","cd","bcd","abcd"]
 * 输出：4 
 * 解释：这两个单词为 "ab", "cd"。
 * 
 * 示例 3：
 * 
 * 
 * 输入：words = ["a","aa","aaa","aaaa"]
 * 输出：0 
 * 解释：不存在这样的两个单词。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 2 <= words.length <= 1000
 * 1 <= words[i].length <= 1000
 * words[i] 仅包含小写字母
 * 
 * 
 */

// @lc code=start
class Solution {
    public int maxProduct(String[] words) {
        int n = words.length;
        int[] ws = new int[n];

        for (int i = 0; i < n; i++) {
            String w = words[i];
            int t = 0;
            for (char c : w.toCharArray()) {
                int j = c - 'a';
                t |= (1 << j);
            }
            ws[i] = t;
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int k1 = ws[i];
                int k2 = ws[j];
                if ((k1 & k2) == 0) {
                    ans = Math.max(ans, words[i].length() * words[j].length());
                }
            }
        }

        return ans;

    }
}
// @lc code=end
