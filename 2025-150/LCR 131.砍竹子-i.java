/*
 * @lc app=leetcode.cn id=LCR 131 lang=java
 * @lcpr version=30204
 *
 * [LCR 131] 砍竹子 I
 *
 * https://leetcode.cn/problems/jian-sheng-zi-lcof/description/
 *
 * algorithms
 * Medium (57.36%)
 * Likes:    630
 * Dislikes: 0
 * Total Accepted:    309.5K
 * Total Submissions: 539.5K
 * Testcase Example:  '12'
 *
 * 现需要将一根长为正整数 bamboo_len 的竹子砍为若干段，每段长度均为正整数。请返回每段竹子长度的最大乘积是多少。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入: bamboo_len = 12
 * 输出: 81
 * 
 * 提示：
 * 
 * 
 * 2 <= bamboo_len <= 58
 * 
 * 
 * 注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/
 * 
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
class Solution {
    int ans = 0;
    Map<Integer, Integer> ansMap = new HashMap<>();
    public int cuttingBamboo(int bamboo_len) {
        return dfs(bamboo_len);
    }

    private int dfs(int b) {
        if (b == 2) {
            return 1;
        }
        if (ansMap.containsKey(b)) {
            return ansMap.get(b);
        }
        int ans = -1;
        
        for (int i = 1; i < b; i++) {
            ans = Math.max(ans, Math.max(i * (b-i), i * dfs(b-i)));
        }
        ansMap.put(b, ans);
        return ans;
        
    }
}
// @lc code=end



/*
// @lcpr case=start
// 12\n
// @lcpr case=end

 */

