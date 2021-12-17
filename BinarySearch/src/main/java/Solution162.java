public class Solution162 {
    public int findPeakElement(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int lmid = (left + right) / 2;
            int rmid = lmid + 1;

            if (nums[rmid] <= nums[lmid]) {
                right = lmid;
            } else {
                left = lmid + 1;
            }
        }
        return right;

    }

    public static void main(String[] args) {
        Solution162 s = new Solution162();

        // int[] nums = { 1, 2, 3, 1 }; // 2
        int[] nums = { 1, 2, 1, 3, 5, 6, 4 }; // 1 or 5
        int res = s.findPeakElement(nums);
        System.out.println(res);
    }
}
