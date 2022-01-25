package bfs;

import java.util.*;

public class Solution2045 {
    public int secondMinimum(int n, int[][] edges, int time, int change) {

        List<Integer>[] to = new ArrayList[n + 1];

        for (int i = 0; i < n + 1; i++) {
            to[i] = new ArrayList<>();
        }

        for (int[] edge : edges) {
            int x = edge[0];
            int y = edge[1];
            to[x].add(y);
            to[y].add(x);
        }

        int[][] dist = new int[n + 1][2];

        for (int i = 0; i < dist.length; i++) {
            dist[i][0] = Integer.MAX_VALUE;
            dist[i][1] = Integer.MAX_VALUE;
        }

        dist[1][0] = 0;
        Queue<int[]> pq = new ArrayDeque<>();
        pq.offer(new int[] { 1, 0 });

        while (dist[n][1] == Integer.MAX_VALUE) {
            int[] nodeDisPair = pq.poll();
            int node = nodeDisPair[0];
            int distance = nodeDisPair[1];

            int nextDistance = distance + 1;

            for (int nextNode : to[node]) {
                if (nextDistance < dist[nextNode][0]) {
                    dist[nextNode][0] = nextDistance;
                    pq.offer(new int[] { nextNode, nextDistance });
                }
                if (nextDistance > dist[nextNode][0] && nextDistance < dist[nextNode][1]) {
                    dist[nextNode][1] = nextDistance;
                    pq.offer(new int[] { nextNode, nextDistance });
                }
            }
        }

        int ans = 0;

        for (int i = 0; i < dist[n][1]; i++) {
            if (ans % (change * 2) >= change) {
                ans = ans + (change * 2 - ans % (2 * change));
            }

            ans += time;

        }
        return ans;

    }

}
