public class Solution34 {

    public int[] searchRange(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int[] ans = { -1, -1 };

        while (left < right) {
            int mid = (left + right + 1) / 2;
            if (nums[mid] <= target) {
                left = mid;
            } else {
                right = mid - 1;
            }

        }
        if (nums[right] == target) {
            ans[1] = right;
        }

        left = 0;
        right = nums.length - 1;
        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }

        }
        if (nums[right] == target) {
            ans[1] = right;
        }

        return ans;
    }

    public static void main(String[] args) {
        Solution34 s = new Solution34();
        // int[] nums = { 5, 7, 7, 8, 8, 10 };
        // int target = 6;
        // int[] nums = {};
        int[] nums = { 1 };
        int target = 1;

        int[] res = s.searchRange(nums, target);

        for (int i : res) {
            System.out.print(i + " ");
        }
    }
}
