/*
 * @lc app=leetcode.cn id=2603 lang=java
 *
 * [2603] 收集树中金币
 *
 * https://leetcode.cn/problems/collect-coins-in-a-tree/description/
 *
 * algorithms
 * Hard (43.47%)
 * Likes:    105
 * Dislikes: 0
 * Total Accepted:    8.2K
 * Total Submissions: 14.3K
 * Testcase Example:  '[1,0,0,0,0,1]\n[[0,1],[1,2],[2,3],[3,4],[4,5]]'
 *
 * 给你一个 n 个节点的无向无根树，节点编号从 0 到 n - 1 。给你整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中
 * edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间有一条边。再给你一个长度为 n 的数组 coins ，其中 coins[i]
 * 可能为 0 也可能为 1 ，1 表示节点 i 处有一个金币。
 * 
 * 一开始，你需要选择树中任意一个节点出发。你可以执行下述操作任意次：
 * 
 * 
 * 收集距离当前节点距离为 2 以内的所有金币，或者
 * 移动到树中一个相邻节点。
 * 
 * 
 * 你需要收集树中所有的金币，并且回到出发节点，请你返回最少经过的边数。
 * 
 * 如果你多次经过一条边，每一次经过都会给答案加一。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 输入：coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]
 * 输出：2
 * 解释：从节点 2 出发，收集节点 0 处的金币，移动到节点 3 ，收集节点 5 处的金币，然后移动回节点 2 。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 
 * 输入：coins = [0,0,0,1,1,0,0,1], edges =
 * [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]
 * 输出：2
 * 解释：从节点 0 出发，收集节点 4 和 3 处的金币，移动到节点 2 处，收集节点 7 处的金币，移动回节点 0 。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * n == coins.length
 * 1 <= n <= 3 * 10^4
 * 0 <= coins[i] <= 1
 * edges.length == n - 1
 * edges[i].length == 2
 * 0 <= ai, bi < n
 * ai != bi
 * edges 表示一棵合法的树。
 * 
 * 
 */

// @lc code=start
import java.util.*;

class Solution {
    public int collectTheCoins(int[] coins, int[][] edges) {
        int n = coins.length;
        HashMap<Integer, HashSet<Integer>> graph = new HashMap<>();
        int[] deg = new int[n];
        int[] deleted = new int[n];

        for (int i = 0; i < edges.length; i++) {
            int[] edge = edges[i];
            int x = edge[0];
            int y = edge[1];
            graph.compute(x, (k, v) -> {
                if (v == null) {
                    return new HashSet<>(Set.of(y));
                } else {
                    v.add(y);
                    return v;
                }
            });
            graph.compute(y, (k, v) -> {
                if (v == null) {
                    return new HashSet<>(Set.of(x));
                } else {
                    v.add(x);
                    return v;
                }
            });

            deg[x]++;
            deg[y]++;
        }
        System.out.println(graph);

        ArrayDeque<Integer> deque = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            if (deg[i] == 1 && coins[i] == 0) {
                deque.push(i);
            }
        }

        while (deque.size() != 0) {
            Integer first = deque.pollFirst();
            deleted[first] = 1;
            deg[first]--;

            for (Integer to : graph.get(first)) {
                if (--deg[to] == 1 && coins[to] == 0) {
                    deque.push(to);
                }
            }
        }

        for (int k = 0; k < 2; k++) {
            ArrayDeque<Integer> dq = new ArrayDeque<>();
            for (int i = 0; i < n; i++) {
                if (deg[i] == 1) {
                    dq.add(i);
                }
            }
            for (Integer x : dq) {
                deg[x]--;
                deleted[x] = 1;
                for (Integer to : graph.get(x)) {
                    deg[to]--;
                }
            }
            // while (dq.size() != 0) {
            // Integer first = dq.pollFirst();
            // deg[first]--;
            // deleted[first] = 1;
            // for (Integer to: graph.get(first)) {
            // deg[to]--;
            // }
            // }
        }
        int cnt = Arrays.stream(deleted).sum();
        return Math.max(0, (n - cnt - 1) * 2);
    }

}
// @lc code=end
