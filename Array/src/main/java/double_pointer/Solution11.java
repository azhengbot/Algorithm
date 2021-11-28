package double_pointer;

public class Solution11 {
    public int maxArea(int[] height) {
        int start = 0;
        int end = height.length-1;
        int ans = 0;

        while (start < end) {
            if (height[start] <= height[end]) {
                ans = Math.max(ans, height[start] * (end - start));
                start++;
            } else {
                ans = Math.max(ans, height[end] * (end - start));
                end--;
            }

        }
        return ans;
    }

    public static void main(String[] args) {
        int[] heights = { 1, 8, 6, 2, 5, 4, 8, 3, 7 };
        Solution11 s = new Solution11();

        int res = s.maxArea(heights);
        System.out.println(res);

    }

}
