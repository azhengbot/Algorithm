import java.util.Random;

public class Solution215 {
    private int[] nums;
    private int k;
    private int n;

    public int findKthLargest(int[] nums, int k) {
        this.nums = nums;
        this.k = k;
        this.n = nums.length - 1;

        return quickSort(0, n);
        // System.out.println(nums);

    }

    private int quickSort(int l, int r) {
        if (l >= r)
            return nums[l];

        int pivot = partition(l, r);

        if (pivot >= n - k + 1) {
            return quickSort(l, pivot);

        } else {
            return quickSort(pivot + 1, r);

        }
    }

    private int partition(int l, int r) {
        int pivot = new Random().nextInt(r - l + 1) + l;
        int pivotVal = nums[pivot];

        while (l <= r) {
            while (nums[l] < pivotVal)
                l++;
            while (nums[r] > pivotVal)
                r--;

            if (l == r)
                break;

            if (l < r) {
                int temp = nums[r];
                nums[r] = nums[l];
                nums[l] = temp;
                l++;
                r--;
            }
        }
        return r;
    }

    public static void main(String[] args) {
        Solution215 s = new Solution215();
        int[] nums = { 5, 4, 3, 2, 1 };
        int k = 4;
        int res = s.findKthLargest(nums, k);
        System.out.println(res);
    }
}
