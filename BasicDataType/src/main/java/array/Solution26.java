/*
 * @lc app=leetcode.cn id=26 lang=java
 *
 * [26] 删除有序数组中的重复项
 *
 * https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/description/
 *
 * algorithms
 * Easy (53.64%)
 * Likes:    2430
 * Dislikes: 0
 * Total Accepted:    947.8K
 * Total Submissions: 1.8M
 * Testcase Example:  '[1,1,2]'
 *
 * 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
 * 
 * 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
 * 
 * 
 * 
 * 说明:
 * 
 * 为什么返回数值是整数，但输出的答案是数组呢?
 * 
 * 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
 * 
 * 你可以想象内部操作如下:
 * 
 * 
 * // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
 * int len = removeDuplicates(nums);
 * 
 * // 在函数里修改输入数组对于调用者是可见的。
 * // 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
 * for (int i = 0; i < len; i++) {
 * print(nums[i]);
 * }
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [1,1,2]
 * 输出：2, nums = [1,2]
 * 解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [0,0,1,1,1,2,2,3,3,4]
 * 输出：5, nums = [0,1,2,3,4]
 * 解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4
 * 。不需要考虑数组中超出新长度后面的元素。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 
 * -10^4 
 * nums 已按升序排列
 * 
 * 
 * 
 * 
 */
package array;

// @lc code=start
class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length;
        int len = 1;

        int left = 1;
        int right = 1;

        while (right < n) {
            if (nums[right] == nums[right - 1]) {
                right++;
                continue;
            } else {
                len++;
                nums[left] = nums[right];
                right++;
                left++;
            }
        }
        return len;

    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = { 0, 0, 1, 1, 1, 2, 2, 3, 3, 4 };
        int res = s.removeDuplicates(nums);
        System.out.println(res);
    }
}
// @lc code=end