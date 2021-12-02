import java.util.*;

public class Solution78 {
    public List<List<Integer>> subsets(int[] nums) {
        recur(0, nums);

        return ans;

    }

    List<List<Integer>> ans = new ArrayList<>();
    List<Integer> subAns = new ArrayList<>();

    private void recur(int i, int[] nums) {
        if (i == nums.length) {
            // 需要创建一个新数组
            ans.add(new ArrayList<>(subAns));
            return;
        }

        recur(i + 1, nums);
        subAns.add(nums[i]);
        recur(i + 1, nums);

        subAns.remove(subAns.size() - 1);

    }

    public static void main(String[] args) {
        Solution78 s = new Solution78();
        int[] nums = { 1, 2, 3 };
        List<List<Integer>> res = s.subsets(nums);
        System.out.println(res);
    }
}
