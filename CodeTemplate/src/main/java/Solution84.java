import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

/*
 * @lc app=leetcode.cn id=84 lang=java
 *
 * [84] 柱状图中最大的矩形
 *
 * https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
 *
 * algorithms
 * Hard (43.63%)
 * Likes:    1743
 * Dislikes: 0
 * Total Accepted:    210.1K
 * Total Submissions: 481.3K
 * Testcase Example:  '[2,1,5,6,2,3]'
 *
 * 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
 * 
 * 求在该柱状图中，能够勾勒出来的矩形的最大面积。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 
 * 
 * 
 * 输入：heights = [2,1,5,6,2,3]
 * 输出：10
 * 解释：最大的矩形为图中红色区域，面积为 10
 * 
 * 
 * 示例 2：
 * 
 * 
 * 
 * 
 * 输入： heights = [2,4]
 * 输出： 4
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * 0 
 * 
 * 
 */

// @lc code=start
public class Solution84 {
    public int largestRectangleArea(int[] heights) {

        int[] heightsWithZero = Arrays.copyOf(heights, heights.length + 1);
        heightsWithZero[heights.length] = 0;
        Deque<int[]> stack = new ArrayDeque<>();

        int maxArea = 0;

        for (int height : heightsWithZero) {
            int accumulatedWidth = 0;

            while (!stack.isEmpty() && stack.peekLast()[0] > height) {
                int[] top = stack.pollLast();
                accumulatedWidth += top[1];
                maxArea = Math.max(maxArea, top[0] * accumulatedWidth);
            }

            stack.add(new int[] { height, accumulatedWidth + 1 });
        }
        return maxArea;
    }

    public static void main(String[] args) {
        Solution84 s = new Solution84();
        // int[] heights = { 2, 1, 5, 6, 2, 3 };
        int[] heights = { 2, 4 };
        int res = s.largestRectangleArea(heights);
        System.out.println(res);
    }
}
// @lc code=end
