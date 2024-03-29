/*
 * @lc app=leetcode.cn id=82 lang=java
 *
 * [82] 删除排序链表中的重复元素 II
 *
 * https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/description/
 *
 * algorithms
 * Medium (53.63%)
 * Likes:    1237
 * Dislikes: 0
 * Total Accepted:    390.3K
 * Total Submissions: 725K
 * Testcase Example:  '[1,2,3,3,4,4,5]'
 *
 * 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：head = [1,2,3,3,4,4,5]
 * 输出：[1,2,5]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：head = [1,1,1,2,3]
 * 输出：[2,3]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 链表中节点数目在范围 [0, 300] 内
 * -100 <= Node.val <= 100
 * 题目数据保证链表已经按升序 排列
 * 
 * 
 */

// @lc code=start

import java.util.HashMap;

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
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode(-101);
        ListNode headCopy = head;
        dummy.next = head;

        HashMap<Integer, Integer> cntMap = new HashMap<>();

        while (headCopy != null) {
            cntMap.put(headCopy.val, cntMap.getOrDefault(headCopy.val, 0) + 1);
            headCopy = headCopy.next;
        }

        // System.out.println(cntMap);

        ListNode pre = dummy;
        ListNode cur = dummy.next;

        // System.out.println(cur.val);
        while (cur != null) {
            if (cntMap.get(cur.val) == 1) {
                pre.next = cur;
                pre = cur;
            }
            cur = cur.next;

            if (cur == null) {
                pre.next = null;
            }
        }
        if (pre == dummy) {
            return null;
        }

        return dummy.next;
    }
}
// @lc code=end
