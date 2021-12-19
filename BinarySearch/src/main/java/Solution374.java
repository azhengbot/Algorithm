public class Solution374 {
    private int guess(int num) {
        if (num == pick)
            return 0;
        else if (num > pick)
            return -1;
        else
            return 1;
    }

    public int guessNumber(int n) {
        int left = 1;
        int right = n;

        while (left <= right) {
            // 注意边界问题
            int mid = (int) ((left + 1L + right - 1L) / 2L);

            if (guess(mid) == 0)
                return mid;
            else if (guess(mid) == -1)
                right = mid - 1;
            else
                left = mid + 1;
        }

        return 0;
    }

    public int pick = 1702766719;

    public static void main(String[] args) {
        Solution374 s = new Solution374();
        int n = 2126753390;

        int res = s.guessNumber(n);

        System.out.println(res);
    }
}
