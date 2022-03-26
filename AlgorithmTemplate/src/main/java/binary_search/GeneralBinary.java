package binary_search;

/*
 * @lc app=leetcode.cn id=34 lang=java
 *
 * [34] 在排序数组中查找元素的第一个和最后一个位置
 */

// @lc code=start

class Solution {
    public int[] searchRange(int[] nums, int target) {
        int n = nums.length;
        int[] ans = new int[] { -1, -1 };

        int l = 0;
        int r = n;
        while (l < r) {
            int mid = (l + r) / 2;

            if (nums[mid] >= target) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        ans[0] = l;

        l = -1;
        r = n - 1;
        while (l < r) {
            int mid = (l + r + 1) / 2;

            if (nums[mid] <= target) {
                l = mid;
            } else {
                r = mid - 1;
            }
        }
        ans[1] = r;

        if (ans[1] < ans[0]) {
            return new int[] { -1, -1 };
        }

        return ans;

    }
}
// @lc code=end
