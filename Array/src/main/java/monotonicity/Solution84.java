package monotonicity;

import java.util.ArrayDeque;
import java.util.Arrays;

// https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
public class Solution84 {

    class Rectangle {
        int height;
        int width;

        Rectangle(int height, int width) {
            this.height = height;
            this.width = width;
        }

    }

    private ArrayDeque<Rectangle> stack = new ArrayDeque<>();

    public int largestRectangleArea(int[] heights) {
        int res = 0;

        int[] ints = Arrays.copyOf(heights, heights.length + 1);
        ints[heights.length] = 0;

        for (int height : ints) {
            int accumulateWidth = 0;
            while (!stack.isEmpty() && stack.peek().height >= height) {
                // 只有往回pop的时候，才需要累加宽度
                accumulateWidth += stack.peek().width;
                res = Math.max(res, stack.peek().height * accumulateWidth);
                stack.pop();
            }
            stack.push(new Rectangle(height, accumulateWidth + 1));
        }
        return res;
    }

    public static void main(String[] args) {
        Solution84 solution = new Solution84();
        int[] heights = {2, 1, 5, 6, 2, 3};
        int res = solution.largestRectangleArea(heights);
        System.out.println(res);
    }

}
