#
# @lc app=leetcode.cn id=21 lang=python3
# @lcpr version=30204
#
# [21] 合并两个有序链表
#
# https://leetcode.cn/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (67.15%)
# Likes:    3631
# Dislikes: 0
# Total Accepted:    1.9M
# Total Submissions: 2.8M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
#
#
# 示例 1：
#
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
#
#
# 示例 2：
#
# 输入：l1 = [], l2 = []
# 输出：[]
#
#
# 示例 3：
#
# 输入：l1 = [], l2 = [0]
# 输出：[0]
#
#
#
#
# 提示：
#
#
# 两个链表的节点数目范围是 [0, 50]
# -100 <= Node.val <= 100
# l1 和 l2 均按 非递减顺序 排列
#
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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    node.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    node.next = ListNode(list2.val)
                    list2 = list2.next
            elif list1:
                node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                list2 = list2.next
            node = node.next

        return dummy.next


# @lc code=end


#
# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#
