from platform import node
from typing import List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        pq = []

        for list_node in lists:
            if list_node:
                heapq.heappush(pq, MyNode(list_node.val, list_node))

        print(pq)

        head = ListNode(0, None)
        tail = head

        while len(pq) != 0:
            min_top = heapq.heappop(pq)
            tail.next = min_top.node
            tail = tail.next

            if min_top.node.next:
                heapq.heappush(pq, MyNode(min_top.node.next.val, min_top.node.next))

        return head.next


class MyNode:
    def __init__(self, val=0, node=None):
        self.val = val
        self.node = node

    def __lt__(self, other):
        return self.val < other.val


s = Solution()
s.mergeKLists([[]])