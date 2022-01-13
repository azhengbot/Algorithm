import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Solution1584 {
    private int[] fa;

    public int minCostConnectPoints(int[][] points) {
        int n = points.length;

        List<int[]> edges = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int dis = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
                edges.add(new int[] { i, j, dis });
            }

        }
        edges.sort(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[2] - o2[2];
            }

        });

        int ans = 0;
        fa = new int[n];
        for (int i = 0; i < n; i++) {
            fa[i] = i;
        }

        for (int[] edge : edges) {
            int x = edge[0];
            int y = edge[1];
            int z = edge[2];

            x = find(x);
            y = find(y);

            if (x != y) {
                ans += z;
                fa[x] = y;
            }
        }

        return ans;
    }

    private int find(int x) {
        if (x == fa[x]) {
            return x;
        }
        return fa[x] = find(fa[x]);
    }

    public static void main(String[] args) {

    }
}
