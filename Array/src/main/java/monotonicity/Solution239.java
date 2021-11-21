package monotonicity;

//https://leetcode-cn.com/problems/sliding-window-maximum/

import java.util.ArrayDeque;
import java.util.ArrayList;

public class Solution239 {
    ArrayDeque<Integer> deque = new ArrayDeque<>();

    ArrayList<Integer> res = new ArrayList<>();

    public int[] maxSlidingWindow(int[] nums, int k) {
        for (int i = 0; i < nums.length; i++) {
            while (!deque.isEmpty() && deque.getFirst() <= i - k) {
                deque.removeFirst();
            }

            while (!deque.isEmpty() && nums[deque.getLast()] <= nums[i]) {
                deque.removeLast();
            }
            deque.offer(i);

            System.out.println(deque);
            if (i >= k - 1) {
                res.add(nums[deque.getFirst()]);
            }

        }

        return res.stream().mapToInt(Integer::valueOf).toArray();
    }

    public static void main(String[] args) {
        Solution239 solution = new Solution239();

        int[] nums = {1, 3, 1, 2, 0, 5};
        int k = 3;

        int[] res = solution.maxSlidingWindow(nums, k);

        for (int re : res) {
            System.out.println(re);
        }
    }
}
