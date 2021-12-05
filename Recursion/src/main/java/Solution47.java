import java.util.*;

public class Solution47 {
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums);
        this.nums = nums;
        this.n = nums.length;
        this.used = new boolean[n];
        recur(0);
        return res;
    }

    private void recur(int pos) {

        if (pos == n) {
            res.add(new ArrayList<>(ans));
            return;
        }

        for (int i = 0; i < n; i++) {
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
                continue;
            }

            if (!used[i]) {
                ans.add(nums[i]);
                used[i] = true;
                recur(pos + 1);
                used[i] = false;
                ans.remove(ans.size() - 1);

            }

        }

    }

    private int[] nums;
    private int n;

    private List<List<Integer>> res = new ArrayList<>();
    private List<Integer> ans = new ArrayList<>();
    private boolean[] used;

    public static void main(String[] args) {
        Solution47 s = new Solution47();
        // int[] nums = { 1, 2, 3 };
        int[] nums = { 1, 1, 3 };
        System.out.println(s.permuteUnique(nums));

    }
}
