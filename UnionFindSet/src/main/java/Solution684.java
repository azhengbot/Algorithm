public class Solution684 {
    int[] fa;

    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;
        fa = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            fa[i] = i;
        }

        for (int[] edge : edges) {
            if (find(edge[0]) == find(edge[1])) {
                return edge;
            }

            unionSet(edge[0], edge[1]);
        }
        return edges[0];
    }

    private int find(int x) {
        if (x == fa[x]) {
            return x;
        }
        return fa[x] = find(fa[x]);
    }

    private void unionSet(int x, int y) {
        x = find(x);
        y = find(y);

        if (x != y) {
            fa[x] = y;
        }
    }
}