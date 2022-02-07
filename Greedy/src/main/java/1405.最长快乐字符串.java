import java.util.PriorityQueue;

/*
 * @lc app=leetcode.cn id=1405 lang=java
 *
 * [1405] 最长快乐字符串
 *
 * https://leetcode-cn.com/problems/longest-happy-string/description/
 *
 * algorithms
 * Medium (59.15%)
 * Likes:    113
 * Dislikes: 0
 * Total Accepted:    12.6K
 * Total Submissions: 21.3K
 * Testcase Example:  '1\n1\n7'
 *
 * 如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。
 * 
 * 给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：
 * 
 * 
 * s 是一个尽可能长的快乐字符串。
 * s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
 * s 中只含有 'a'、'b' 、'c' 三种字母。
 * 
 * 
 * 如果不存在这样的字符串 s ，请返回一个空字符串 ""。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：a = 1, b = 1, c = 7
 * 输出："ccaccbcc"
 * 解释："ccbccacc" 也是一种正确答案。
 * 
 * 
 * 示例 2：
 * 
 * 输入：a = 2, b = 2, c = 1
 * 输出："aabbc"
 * 
 * 
 * 示例 3：
 * 
 * 输入：a = 7, b = 1, c = 0
 * 输出："aabaa"
 * 解释：这是该测试用例的唯一正确答案。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 <= a, b, c <= 100
 * a + b + c > 0
 * 
 * 
 */

// @lc code=start
class Solution {
    public String longestDiverseString(int a, int b, int c) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a1, a2) -> a2[0] - a1[0]);
        pq.add(new int[] { a, 0 });
        pq.add(new int[] { b, 1 });
        pq.add(new int[] { c, 2 });

        StringBuilder sb = new StringBuilder();

        while (true) {
            int[] cur = pq.poll();
            if (cur[0] == 0) {
                break;
            }
            int sbLen = sb.length();
            if (sbLen >= 2 && sb.charAt(sbLen - 1) - 'a' == cur[1] && sb.charAt(sbLen - 2) - 'a' == cur[1]) {
                int[] next = pq.poll();
                if (next[0] == 0) {
                    break;
                }
                sb.append((char) (next[1] + 'a'));
                next[0] = next[0] - 1;

                pq.add(next);
                pq.add(cur);

            } else {
                sb.append((char) (cur[1] + 'a'));
                cur[0] = cur[0] - 1;

                pq.add(cur);

            }
        }

        return sb.toString();

    }

    public static void main(String[] args) {
        Solution s = new Solution();
        String res = s.longestDiverseString(1, 1, 7);
        System.out.println(res);
    }
}
// @lc code=end
