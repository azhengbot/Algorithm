package week10;

import java.util.*;

public class Solution239 {
    public int[] maxSlidingWindow(int[] nums, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(
                (o1, o2) -> o1[0] - o2[0]);

        int n = nums.length;

        List<Integer> ans = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            pq.add(new int[] { -nums[i], i });

            if (i >= k - 1) {
                while (pq.peek()[1] < i - k + 1) {
                    pq.poll();
                }
                ans.add(pq.peek()[0]);
            }
        }

        return ans.stream().mapToInt(Integer::valueOf).toArray();
    }

    public static void main(String[] args) {
        Solution239 s = new Solution239();
        int[] nums = { 1, 3, -1, -3, 5, 3, 6, 7 };
        int k = 3;
        int[] res = s.maxSlidingWindow(nums, k);
        System.out.println(res);
    }
}
