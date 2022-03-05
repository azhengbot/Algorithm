
/*
 * @lc app=leetcode.cn id=23 lang=java
 *
 * [23] 合并K个升序链表
 *
 * https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
 *
 * algorithms
 * Hard (56.52%)
 * Likes:    1775
 * Dislikes: 0
 * Total Accepted:    403.3K
 * Total Submissions: 713.2K
 * Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
 *
 * 给你一个链表数组，每个链表都已经按升序排列。
 * 
 * 请你将所有链表合并到一个升序链表中，返回合并后的链表。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：lists = [[1,4,5],[1,3,4],[2,6]]
 * 输出：[1,1,2,3,4,4,5,6]
 * 解释：链表数组如下：
 * [
 * ⁠ 1->4->5,
 * ⁠ 1->3->4,
 * ⁠ 2->6
 * ]
 * 将它们合并到一个有序链表中得到。
 * 1->1->2->3->4->4->5->6
 * 
 * 
 * 示例 2：
 * 
 * 输入：lists = []
 * 输出：[]
 * 
 * 
 * 示例 3：
 * 
 * 输入：lists = [[]]
 * 输出：[]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * k == lists.length
 * 0 <= k <= 10^4
 * 0 <= lists[i].length <= 500
 * -10^4 <= lists[i][j] <= 10^4
 * lists[i] 按 升序 排列
 * lists[i].length 的总和不超过 10^4
 * 
 * 
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

import java.util.*;

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class BinaryHeap {
    List<ListNode> heap;

    public BinaryHeap() {
        this.heap = new ArrayList<>();
        heap.add(new ListNode());
    }

    public boolean isEmpty() {
        return heap.size() <= 1;
    }

    public void push(ListNode node) {
        heap.add(node);
        heapifyUp(heap.size() - 1);
    }

    public ListNode pop() {
        ListNode node = heap.get(1);
        heap.set(1, heap.get(heap.size() - 1));
        heap.remove(heap.size() - 1);
        heapfiyDown(1);
        return node;
    }

    private void heapifyUp(int leaf) {
        while (leaf > 1) {
            int root = leaf / 2;
            if (heap.get(root).val > heap.get(leaf).val) {
                Collections.swap(heap, root, leaf);
                leaf = root;
            } else {
                break;
            }
        }
    }

    private void heapfiyDown(int root) {
        int child = root * 2;

        while (child < heap.size()) {
            int otherChild = child + 1;

            if (otherChild < heap.size() && heap.get(otherChild).val < heap.get(child).val) {
                child = otherChild;
            }

            if (heap.get(child).val < heap.get(root).val) {
                Collections.swap(heap, child, root);
                root = child;
                child = root * 2;
            } else {
                break;
            }
        }
    }
}

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        BinaryHeap bh = new BinaryHeap();

        for (ListNode node : lists) {
            if (node != null) {
                bh.push(node);
            }
        }

        ListNode head = new ListNode();
        ListNode curr = head;

        while (!bh.isEmpty()) {
            ListNode node = bh.pop();
            if (node.next != null) {
                bh.push(node.next);
            }

            curr.next = node;
            curr = curr.next;
        }

        return head.next;
    }
}
// @lc code=end
