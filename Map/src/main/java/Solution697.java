
// https://leetcode-cn.com/problems/degree-of-an-array/
import java.util.HashMap;

public class Solution697 {
    public int findShortestSubArray(int[] nums) {
        HashMap<Integer, Integer[]> resMap = new HashMap<>();
        int maxRes = 0;
        int res = nums.length;

        for (int i = 0; i < nums.length; i++) {
            Integer[] resLst = resMap.getOrDefault(nums[i], new Integer[] { 0, i });
            resLst[0]++;

            resMap.put(nums[i], resLst);

            if (resMap.get(nums[i])[0] > maxRes) {
                maxRes = resMap.get(nums[i])[0];
                res = i - resMap.get(nums[i])[1] + 1;
            }

            if (resMap.get(nums[i])[0] == maxRes) {
                res = Math.min(res, i - resMap.get(nums[i])[1] + 1);
            }
        }

        return res;

    }

    public static void main(String[] args) {
        Solution697 s = new Solution697();
        int[] nums = { 1, 2, 2, 3, 1 };
        int res = s.findShortestSubArray(nums);
        System.out.println(res);
    }
}
