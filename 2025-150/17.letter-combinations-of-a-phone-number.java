/*
 * @lc app=leetcode.cn id=17 lang=java
 * @lcpr version=30204
 *
 * [17] 电话号码的字母组合
 *
 * https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/
 *
 * algorithms
 * Medium (61.33%)
 * Likes:    2994
 * Dislikes: 0
 * Total Accepted:    1M
 * Total Submissions: 1.7M
 * Testcase Example:  '"23"'
 *
 * 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
 * 
 * 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
 * 
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：digits = "23"
 * 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
 * 
 * 
 * 示例 2：
 * 
 * 输入：digits = ""
 * 输出：[]
 * 
 * 
 * 示例 3：
 * 
 * 输入：digits = "2"
 * 输出：["a","b","c"]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 <= digits.length <= 4
 * digits[i] 是范围 ['2', '9'] 的一个数字。
 * 
 * 
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
class Solution {
    List<String> ans = new ArrayList<>();
   Map<Integer, List<String>> dic  = new HashMap<>();
    public List<String> letterCombinations(String digits) {
       dic.put(2, new ArrayList(Arrays.asList("a", "b", "c")));
       dic.put(3, new ArrayList(Arrays.asList("d", "e", "f")));
       dic.put(4, new ArrayList(Arrays.asList("g", "h", "i")));
       dic.put(5, new ArrayList(Arrays.asList("j", "k", "l")));
       dic.put(6, new ArrayList(Arrays.asList("m", "n", "o")));
       dic.put(7, new ArrayList(Arrays.asList("p", "q", "r", "s")));
       dic.put(8, new ArrayList(Arrays.asList("t", "u", "v")));
       dic.put(9, new ArrayList(Arrays.asList("w", "x", "y", "z")));
    //    System.out.println(dic);
        if (digits.length() == 0) {
            return ans;
        }
       dfs(digits, 0, "");
       return ans;

    }

    private void dfs(String digits, int idx, String sub) {
        int n = digits.length();
        if (idx >= n) {
            ans.add(sub);
            return;
        }
        Integer x = digits.charAt(idx) - '0';
        for (String c: dic.get(x)) {
            dfs(digits, idx+1, sub+c);
        }
    }
}
// @lc code=end



/*
// @lcpr case=start
// "23"\n
// @lcpr case=end

// @lcpr case=start
// ""\n
// @lcpr case=end

// @lcpr case=start
// "2"\n
// @lcpr case=end

 */

