package double_pointer;

import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class Solution15 {
    public List<List<Integer>> threeSum(int[] nums) {

        Arrays.sort(nums);

        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            List<List<Integer>> twoNums = getTwoNums(-nums[i], nums, i + 1);

            if (twoNums.size() == 0) {
                continue;
            }
            // System.out.println(twoNums);
            for (List<Integer> l : twoNums) {
                ArrayList<Integer> innerAns = new ArrayList<>(l);
                innerAns.add(nums[i]);
                // System.out.println(innerAns);

                ans.add(innerAns);
            }

        }
        return ans;

    }

    private List<List<Integer>> getTwoNums(int target, int[] nums, int start) {
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = start, j = nums.length - 1; i < j; i++) {
            // 需要i〉start； 如果〉0会把start 也有可能去掉
            if (i > start && nums[i] == nums[i - 1]) {
                continue;
            }

            // 需要 j>i; 否则j会多减一次，导致j=i
            while (j > i && nums[i] + nums[j] > target) {
                j--;
            }
            if (j > i && nums[i] + nums[j] == target) {
                ans.add(Arrays.asList(nums[i], nums[j]));

            }
        }
        return ans;

    }

    public static void main(String[] args) {
        int[] nums = { -1, 0, 1, 2, -1, -4 };
        // int[] nums = { 0, 1, 1 };
        // int[] nums = { 0, 0, 0, 0 };
        // int[] nums = { 1, 2, -2, -1 };
        Solution15 s = new Solution15();
        List<List<Integer>> res = s.threeSum(nums);

        System.out.println(res);
    }
}
