/*
 * @lc app=leetcode.cn id=307 lang=java
 *
 * [307] 区域和检索 - 数组可修改
 *
 * https://leetcode-cn.com/problems/range-sum-query-mutable/description/
 *
 * algorithms
 * Medium (52.62%)
 * Likes:    442
 * Dislikes: 0
 * Total Accepted:    41.2K
 * Total Submissions: 82.4K
 * Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
 *
 * 给你一个数组 nums ，请你完成两类查询。
 * 
 * 
 * 其中一类查询要求 更新 数组 nums 下标对应的值
 * 另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right
 * 
 * 
 * 实现 NumArray 类：
 * 
 * 
 * NumArray(int[] nums) 用整数数组 nums 初始化对象
 * void update(int index, int val) 将 nums[index] 的值 更新 为 val
 * int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含
 * ）的nums元素的 和 （即，nums[left] + nums[left + 1], ..., nums[right]）
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：
 * ["NumArray", "sumRange", "update", "sumRange"]
 * [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
 * 输出：
 * [null, 9, null, 8]
 * 
 * 解释：
 * NumArray numArray = new NumArray([1, 3, 5]);
 * numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
 * numArray.update(1, 2);   // nums = [1,2,5]
 * numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= nums.length <= 3 * 10^4
 * -100 <= nums[i] <= 100
 * 0 <= index < nums.length
 * -100 <= val <= 100
 * 0 <= left <= right < nums.length
 * 调用 update 和 sumRange 方法次数不大于 3 * 10^4 
 * 
 * 
 */

// @lc code=start
class Node {
    int l;
    int r;
    int data;

    public Node() {

    }

    public Node(int l, int r) {
        this.l = l;
        this.r = r;
    }

    public Node(int l, int r, int data) {
        this.l = l;
        this.r = r;
        this.data = data;
    }
}

class SegmentTree {
    Node[] tree;
    int n;
    int[] nums;

    public SegmentTree(int[] nums) {
        this.nums = nums;
        this.n = nums.length;
        this.tree = new Node[4 * n];
        build(1, 0, n - 1);
    }

    public void build(int p, int l, int r) {
        // System.out.println(p + " " + l + " " + r);
        if (l == r) {
            tree[p] = new Node(l, r, nums[l]);
            return;
        }

        int mid = (l + r) / 2;

        build(p * 2, l, mid);
        build(p * 2 + 1, mid + 1, r);
        // System.out.println(tree[p]);
        tree[p] = new Node(l, r);
        tree[p].data = tree[2 * p].data + tree[2 * p + 1].data;
    }

    public void update(int p, int idx, int val) {
        int l = tree[p].l;
        int r = tree[p].r;
        if (l == r) {
            tree[p].data = val;
            return;
        }
        int mid = (l + r) / 2;

        if (idx <= mid) {
            update(2 * p, idx, val);
        } else {
            update(2 * p + 1, idx, val);
        }
        tree[p].data = tree[2 * p].data + tree[2 * p + 1].data;
    }

    public int query(int p, int left, int right) {
        int l = tree[p].l;
        int r = tree[p].r;

        if (left <= l && r <= right) {
            return tree[p].data;
        }

        int mid = (l + r) / 2;
        int ans = 0;
        if (left <= mid) {
            ans += query(2 * p, left, right);
        }
        if (right > mid) {
            ans += query(2 * p + 1, left, right);
        }
        return ans;
    }
}

class NumArray {
    SegmentTree st;

    public NumArray(int[] nums) {
        this.st = new SegmentTree(nums);
    }

    public void update(int index, int val) {
        st.update(1, index, val);
    }

    public int sumRange(int left, int right) {
        return st.query(1, left, right);
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(index,val);
 * int param_2 = obj.sumRange(left,right);
 */
// @lc code=end
