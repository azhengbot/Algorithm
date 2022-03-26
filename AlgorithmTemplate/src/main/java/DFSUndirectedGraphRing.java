/*
 * @lc app=leetcode.cn id=684 lang=java
 *
 * [684] 冗余连接
 *
 * https://leetcode-cn.com/problems/redundant-connection/description/
 *
 * algorithms
 * Medium (66.77%)
 * Likes:    432
 * Dislikes: 0
 * Total Accepted:    67.8K
 * Total Submissions: 101.5K
 * Testcase Example:  '[[1,2],[1,3],[2,3]]'
 *
 * 树可以看成是一个连通且 无环 的 无向 图。
 * 
 * 给定往一棵 n 个节点 (节点值 1～n) 的树中添加一条边后的图。添加的边的两个顶点包含在 1 到 n
 * 中间，且这条附加的边不属于树中已存在的边。图的信息记录于长度为 n 的二维数组 edges ，edges[i] = [ai, bi] 表示图中在 ai
 * 和 bi 之间存在一条边。
 * 
 * 请找出一条可以删去的边，删除后可使得剩余部分是一个有着 n 个节点的树。如果有多个答案，则返回数组 edges 中最后出现的边。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 
 * 输入: edges = [[1,2], [1,3], [2,3]]
 * 输出: [2,3]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 
 * 
 * 输入: edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
 * 输出: [1,4]
 * 
 * 
 * 
 * 
 * 提示:
 * 
 * 
 * n == edges.length
 * 3 
 * edges[i].length == 2
 * 1 
 * ai != bi
 * edges 中无重复元素
 * 给定的图是连通的 
 * 
 * 
 */

// @lc code=start
import java.util.*;

class Solution684 {
    List<List<Integer>> to;
    boolean isCycle = false;
    boolean[] used;

    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;
        this.to = new ArrayList<>();
        // [false, false, ...]
        this.used = new boolean[n + 1];
        // 模板：出边数组初始化       
        // 初态：[[], [], ... []]
        for (int i = 0; i < n + 1; i++) {
            to.add(new ArrayList<>());
        }

        for (int[] edge : edges) {
            // 加边
            // 无向图看作双向边的有向图
            to.get(edge[0]).add(edge[1]);
            to.get(edge[1]).add(edge[0]);
            used = new boolean[n + 1];
            dfs(edge[0], -1);

            if (isCycle) {
                return edge;
            }
        }
        return new int[] {};
    }

    // 模板：无向图深度优先遍历找环   
    // visit数组，避免重复访问   
    // fa是第一次走到x的点
    private void dfs(int x, int parent) {
        // 第一步：标记已访问
        used[x] = true;
        // 第二步：遍历所有出边
        for (int can_to : to.get(x)) {
            if (can_to == parent) {
                continue; // 是父节点，不是环
            }
            if (used[can_to]) {
                isCycle = true;
                return;
            }
            dfs(can_to, x);
        }
    }

}
// @lc code=end
