
/*
 * @lc app=leetcode.cn id=78 lang=java
 *
 * [78] 子集
 *
 * https://leetcode-cn.com/problems/subsets/description/
 *
 * algorithms
 * Medium (80.32%)
 * Likes:    1491
 * Dislikes: 0
 * Total Accepted:    377.6K
 * Total Submissions: 470K
 * Testcase Example:  '[1,2,3]'
 *
 * 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
 * 
 * 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [1,2,3]
 * 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [0]
 * 输出：[[],[0]]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * -10 
 * nums 中的所有元素 互不相同
 * 
 * 
 */

// @lc code=start
import java.util.*;

class Solution78 {
    private int n;
    private List<List<Integer>> ans = new ArrayList<>();
    private List<Integer> subAns = new ArrayList<>();
    private int[] nums;

    public List<List<Integer>> subsets(int[] nums) {
        this.n = nums.length;
        this.nums = nums;
        dfs(0);
        return ans;
    }

    private void dfs(int idx) {
        if (idx >= n) {
            ans.add(new ArrayList<>(subAns));
            return;
        }

        dfs(idx + 1);
        subAns.add(nums[idx]);
        dfs(idx + 1);
        subAns.remove(subAns.size() - 1);
    }
}
// @lc code=end
