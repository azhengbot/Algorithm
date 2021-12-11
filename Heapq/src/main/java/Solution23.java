import common.ListNode;
import java.util.*;

public class Solution23 {

    public ListNode mergeKLists(ListNode[] lists) {

        class MyNode implements Comparable<MyNode> {
            int val;
            ListNode node;

            MyNode(int val, ListNode node) {
                this.val = val;
                this.node = node;
            }

            @Override
            public int compareTo(MyNode o) {
                return this.val - o.val;
            }

        }

        PriorityQueue<MyNode> queue = new PriorityQueue<MyNode>();

        for (ListNode listNode : lists) {
            if (listNode != null) {
                queue.offer(new MyNode(listNode.val, listNode));
            }
        }
        ListNode head = new ListNode(0);
        ListNode tail = head;

        while (!queue.isEmpty()) {
            MyNode min = queue.poll();

            tail.next = min.node;
            tail = tail.next;

            if (min.node.next != null) {
                queue.offer(new MyNode(min.node.next.val, min.node.next));
            }
        }
        return head.next;
    }
}