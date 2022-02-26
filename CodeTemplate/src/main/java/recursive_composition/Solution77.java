package recursive_composition;

/*
 * @lc app=leetcode.cn id=77 lang=java
 *
 * [77] 组合
 *
 * https://leetcode-cn.com/problems/combinations/description/
 *
 * algorithms
 * Medium (76.97%)
 * Likes:    872
 * Dislikes: 0
 * Total Accepted:    284.2K
 * Total Submissions: 369.3K
 * Testcase Example:  '4\n2'
 *
 * 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
 * 
 * 你可以按 任何顺序 返回答案。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：n = 4, k = 2
 * 输出：
 * [
 * ⁠ [2,4],
 * ⁠ [3,4],
 * ⁠ [2,3],
 * ⁠ [1,2],
 * ⁠ [1,3],
 * ⁠ [1,4],
 * ]
 * 
 * 示例 2：
 * 
 * 
 * 输入：n = 1, k = 1
 * 输出：[[1]]
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * 1 
 * 
 * 
 */

// @lc code=start
import java.util.*;

class Solution {
    private List<List<Integer>> ans = new ArrayList<>();
    private List<Integer> subAns = new ArrayList<>();
    private int n;
    private int k;

    public List<List<Integer>> combine(int n, int k) {
        this.n = n;
        this.k = k;

        dfs(1);
        return ans;
    }

    private void dfs(int idx) {
        if (idx > n + 1 || (subAns.size() + (n - idx + 1) < k)) {
            return;
        }
        if (subAns.size() == k) {
            ans.add(new ArrayList<>(subAns));
            return;
        }

        dfs(idx + 1);
        subAns.add(idx);
        dfs(idx + 1);
        subAns.remove(subAns.size() - 1);

    }
}
// @lc code=end
