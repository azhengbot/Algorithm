import java.util.HashMap;

public class Solution01 {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> dict = new HashMap<>();

        int[] res = new int[2];
        for (int i=0; i<nums.length; i++) {
            int needValue = target - nums[i];
            if (dict.containsKey(needValue)) {
                res[0] = dict.get(needValue);
                res[1] = i;
                return res;
            }
            dict.put(nums[i], i);
        }
        return res;
    }
}
