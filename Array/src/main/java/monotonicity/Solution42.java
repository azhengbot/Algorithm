package monotonicity;

import java.util.*;

public class Solution42 {
    public int trap(int[] height) {
        int ans = 0;

        Deque<int[]> stack = new ArrayDeque<>();

        for (int h : height) {
            int accmulateWidth = 0;

            while (!stack.isEmpty() && stack.peek()[0] <= h) {
                int bottom = stack.peek()[0];
                accmulateWidth += stack.peek()[1];

                stack.pop();

                if (stack.isEmpty())
                    continue;

                int up = Math.min(h, stack.peek()[0]);

                ans += accmulateWidth * (up - bottom);

            }
            stack.push(new int[] { h, accmulateWidth + 1 });
            // System.out.println(stack);

        }

        return ans;

    }

    public static void main(String[] args) {
        Solution42 s = new Solution42();
        int[] height = { 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 };
        int res = s.trap(height);
        System.out.println(res);
    }
}
