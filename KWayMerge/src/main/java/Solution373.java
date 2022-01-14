import java.util.*;

class Solution373 {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {

        int n1 = nums1.length;
        int n2 = nums2.length;

        List<List<Integer>> ans = new ArrayList<>();

        PriorityQueue<int[]> pq = new PriorityQueue<>(
                new Comparator<int[]>() {
                    @Override
                    public int compare(int[] o1, int[] o2) {
                        return o1[0] - o2[0];
                    }

                });

        for (int i = 0; i < n1; i++) {
            pq.add(new int[] { nums1[i] + nums2[0], i, 0 });
        }

        while (ans.size() < k && !pq.isEmpty()) {
            int[] l = pq.poll();
            int i = l[1];
            int j = l[2];

            List<Integer> content = new ArrayList<>();

            content.add(nums1[i]);
            content.add(nums2[j]);

            ans.add(content);

            if (j + 1 < n2) {
                pq.add(new int[] { nums1[i] + nums2[j + 1], i, j + 1 });
            }

        }
        return ans;

    }
}