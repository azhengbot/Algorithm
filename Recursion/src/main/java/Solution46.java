/*
 * @lc app=leetcode.cn id=46 lang=java
 *
 * [46] 全排列
 *
 * https://leetcode.cn/problems/permutations/description/
 *
 * algorithms
 * Medium (78.95%)
 * Likes:    2705
 * Dislikes: 0
 * Total Accepted:    934K
 * Total Submissions: 1.2M
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

import java.util.ArrayList;
import java.util.List;

class Solution {
    List<List<Integer>> ans = new ArrayList<>();
    int n;
    boolean[] used;
    List<Integer> subAns = new ArrayList<>();
    int[] nums;

    void dfs(int i) {
        if (i >= n) {
            // System.out.println(subAns);
            ans.add(new ArrayList<>(subAns));
            // System.out.println(ans);
            return;
        }

        for (int j = 0; j < n; j++) {
            if (!used[j]) {
                subAns.add(nums[j]);
                used[j] = true;
                dfs(i + 1);
                used[j] = false;
                subAns.remove(subAns.size() - 1);

            }
        }
    }

    public List<List<Integer>> permute(int[] nums) {
        this.nums = nums;
        n = nums.length;
        used = new boolean[n];
        dfs(0);
        // System.out.println(ans);
        return ans;

    }
}
// @lc code=end
