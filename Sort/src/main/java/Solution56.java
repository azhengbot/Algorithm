import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import java.util.Comparator;

public class Solution56 {
    public int[][] merge(int[][] intervals) {

        int n = intervals.length;

        Arrays.sort(intervals, new Comparator<int[]>() {
            public int compare(int[] interval1, int[] interval2) {
                return interval1[0] - interval2[0];
            }
        });
        List<int[]> ans = new ArrayList<>();

        int start0 = intervals[0][0];
        int start1 = intervals[0][1];
        int i = 0;
        while (i < n) {
            if (intervals[i][0] < start1) {
                if (intervals[i][1] > start1) {
                    start1 = intervals[i][1];
                }
            } else if (intervals[i][0] > start1) {
                ans.add(new int[] { start0, start1 });
                start0 = intervals[i][0];
                start1 = intervals[i][1];
            } else {
                start1 = intervals[i][1];
            }
            i++;
        }
        ans.add(new int[] { start0, start1 });

        return ans.toArray(new int[ans.size()][]);
    }

    public static void main(String[] args) {

    }
}
