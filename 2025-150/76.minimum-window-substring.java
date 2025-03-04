/*
 * @lc app=leetcode.cn id=76 lang=java
 * @lcpr version=30204
 *
 * [76] 最小覆盖子串
 *
 * https://leetcode.cn/problems/minimum-window-substring/description/
 *
 * algorithms
 * Hard (46.88%)
 * Likes:    3160
 * Dislikes: 0
 * Total Accepted:    726.1K
 * Total Submissions: 1.5M
 * Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
 *
 * 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 ""
 * 。
 * 
 * 
 * 
 * 注意：
 * 
 * 
 * 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
 * 如果 s 中存在这样的子串，我们保证它是唯一的答案。
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：s = "ADOBECODEBANC", t = "ABC"
 * 输出："BANC"
 * 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
 * 
 * 
 * 示例 2：
 * 
 * 输入：s = "a", t = "a"
 * 输出："a"
 * 解释：整个字符串 s 是最小覆盖子串。
 * 
 * 
 * 示例 3:
 * 
 * 输入: s = "a", t = "aa"
 * 输出: ""
 * 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
 * 因此没有符合条件的子字符串，返回空字符串。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * ^m == s.length
 * ^n == t.length
 * 1 <= m, n <= 10^5
 * s 和 t 由英文字母组成
 * 
 * 
 * 
 * 进阶：你能设计一个在 o(m+n) 时间内解决此问题的算法吗？
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
class Solution {
    public String minWindow(String s, String t) {
        int[] cntT = new int[128];
        int[] cntS = new int[128];
        Set<Character> setT = new HashSet<>();
        for (char c: t.toCharArray()) {
            cntT[c]++;
            setT.add(c);
        }
        int m = setT.size();
        int n = s.length();
        int left = -1, right = n;
        int i = 0;
        for (int j=0; j<n; j++) {
            char sc = s.charAt(j);
            cntS[sc]++;
            if (cntS[sc] == cntT[sc]) {
                m -= 1;
            }
            while (m == 0) {
                if (j - i < right - left) {
                    left = i;
                    right = j;
                }
                char x = s.charAt(i);
                if (cntS[x] == cntT[x]) {
                    m += 1;
                }
                cntS[x] -= 1;
                i++;
            }
        }

        return left > -1 ? s.substring(left, right+1) : "";
    }
}
// @lc code=end



/*
// @lcpr case=start
// "ADOBECODEBANC"\n"ABC"\n
// @lcpr case=end

// @lcpr case=start
// "a"\n"a"\n
// @lcpr case=end

// @lcpr case=start
// "a"\n"aa"\n
// @lcpr case=end

 */

