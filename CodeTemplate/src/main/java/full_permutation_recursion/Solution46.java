package full_permutation_recursion;

/*
 * @lc app=leetcode.cn id=46 lang=java
 *
 * [46] 全排列
 *
 * https://leetcode-cn.com/problems/permutations/description/
 *
 * algorithms
 * Medium (78.49%)
 * Likes:    1784
 * Dislikes: 0
 * Total Accepted:    519.9K
 * Total Submissions: 662.4K
 * Testcase Example:  '[1,2,3]'
 *
 * 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [1,2,3]
 * 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [0,1]
 * 输出：[[0,1],[1,0]]
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：nums = [1]
 * 输出：[[1]]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= nums.length <= 6
 * -10 <= nums[i] <= 10
 * nums 中的所有整数 互不相同
 * 
 * 
 */

// @lc code=start
import java.util.List;
import java.util.ArrayList;

class Solution {
    private int n;
    private List<Integer> subAns = new ArrayList<>();
    private List<List<Integer>> ans = new ArrayList<>();
    private int[] used;
    private int[] nums;

    public List<List<Integer>> permute(int[] nums) {
        this.n = nums.length;
        this.used = new int[n];
        this.nums = nums;

        dfs(0);

        return ans;
    }

    private void dfs(int idx) {
        if (idx == n) {
            ans.add(new ArrayList<>(subAns));
            return;
        }

        for (int i = 0; i < n; i++) {
            if (used[i] == 1) {
                continue;
            }
            subAns.add(nums[i]);
            used[i] = 1;
            dfs(idx + 1);
            used[i] = 0;
            subAns.remove(subAns.size() - 1);
        }
    }
}
// @lc code=end
