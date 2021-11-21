package monotonicity;

import monotonicity.common.ListNode;


//https://leetcode-cn.com/problems/merge-two-sorted-lists/
public class Solution21 {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode newListNode = new ListNode();

        ListNode p = newListNode;
        ListNode p1 = l1;
        ListNode p2 = l2;

        while (p1!=null && p2!=null) {
            if (p1.val < p2.val) {
                p.next = p1;
                p1=p1.next;
            } else {
                p.next = p2;
                p2=p2.next;
            }
            p = p.next;
        }

        if (p1 != null) {
            p.next = p1;
        }

        if (p2 != null) {
            p.next = p2;
        }

        return newListNode.next;
    }
}
