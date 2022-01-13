package floyd;

public class Solution1334 {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {

        int[][] matrix = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    matrix[i][j] = 0;
                } else {
                    matrix[i][j] = 10000 * 100; // 不能用max_value
                }
            }
        }

        for (int[] edge : edges) {
            int x = edge[0];
            int y = edge[1];
            int z = edge[2];

            matrix[x][y] = matrix[y][x] = z;
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    matrix[i][j] = Math.min(matrix[i][j], matrix[i][k] + matrix[k][j]);
                }
            }
        }

        int ans = 0;
        int minNeighbour = n;

        for (int i = 0; i < n; i++) {
            int neighbour = 0;

            for (int j = 0; j < n; j++) {
                if (i != j && matrix[i][j] <= distanceThreshold) {
                    neighbour++;
                }
            }

            if (neighbour < minNeighbour || (neighbour == minNeighbour && i > ans)) {

                minNeighbour = neighbour;
                ans = i;

            }

        }

        return ans;

    }

    public static void main(String[] args) {

    }
}
