# STUCK
# @lc app=leetcode.cn id=148 lang=python3
# @lcpr version=30204
#
# [148] 排序链表
#
# https://leetcode.cn/problems/sort-list/description/
#
# algorithms
# Medium (66.14%)
# Likes:    2389
# Dislikes: 0
# Total Accepted:    584.4K
# Total Submissions: 882.1K
# Testcase Example:  '[4,2,1,3]'
#
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
#
#
#
#
#
#
# 示例 1：
#
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#
#
# 示例 2：
#
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
#
#
# 示例 3：
#
# 输入：head = []
# 输出：[]
#
#
#
#
# 提示：
#
#
# 链表中节点的数目在范围 [0, 5 * 10^4] 内
# -10^5 <= Node.val <= 10^5
#
#
#
#
# 进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
#
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
    def get_head2(self, head):
        slow = head
        fast = head
        while slow.next and fast.next and fast.next.next:
            # print(slow)
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid

    def head_merge(self, head, head2):
        dummy = ListNode()
        curr = dummy
        while head and head2:
            if head.val < head2.val:
                curr.next = head
                head = head.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
        if head:
            curr.next = head
        if head2:
            curr.next = head2
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        head2 = self.get_head2(head)
        # print(head2)
        head = self.sortList(head)
        head2 = self.sortList(head2)

        return self.head_merge(head, head2)


# @lc code=end


#
# @lcpr case=start
# [4,2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [-1,5,3,4,0]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
