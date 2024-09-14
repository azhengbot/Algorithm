#
# @lc app=leetcode.cn id=2181 lang=python3
# @lcpr version=30204
#
# [2181] 合并零之间的节点
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        dummy = ListNode()
        node = ListNode()
        dummy.next = node
        ans = 0
        cur = cur.next
        while cur:
            if cur.val == 0:
                print(ans)
                node.val = ans
                if not cur.next:
                    break
                node.next = ListNode()
                node = node.next
                cur = cur.next
                ans = 0
                continue
            ans += cur.val
            cur = cur.next

        return dummy.next


# @lc code=end


#
# @lcpr case=start
# [0,3,1,0,4,5,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,3,0,2,2,0]\n
# @lcpr case=end

#
