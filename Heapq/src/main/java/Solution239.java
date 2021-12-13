import java.util.*;

public class Solution239 {
    public int[] maxSlidingWindow(int[] nums, int k) {

        class Pair implements Comparable<Pair> {
            int value;
            int idx;

            Pair(int value, int idx) {
                this.value = value;
                this.idx = idx;
            }

            @Override
            public int compareTo(Pair o) {
                // TODO Auto-generated method stub
                return this.value - o.value;
            }

        }

        PriorityQueue<Pair> queue = new PriorityQueue<>();

        int n = nums.length;
        ArrayList<Integer> ans = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            queue.offer(new Pair(nums[i], i));

            if (i >= k - 1) {
                while (queue.peek().idx <= i - k) {
                    queue.poll();
                }
                ans.add(queue.peek().value);
            }

        }

        return ans.stream().mapToInt(Integer::valueOf).toArray();
    }

}
