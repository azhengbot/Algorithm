#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30204
#
# [2] 两数相加
#
# https://leetcode.cn/problems/add-two-numbers/description/
#
# algorithms
# Medium (44.37%)
# Likes:    10859
# Dislikes: 0
# Total Accepted:    2.2M
# Total Submissions: 5M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
#
#
# 示例 1：
#
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
#
#
# 示例 2：
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#
#
# 示例 3：
#
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
#
#
#
#
# 提示：
#
#
# 每个链表中的节点数在范围 [1, 100] 内
# 0 <= Node.val <= 9
# 题目数据保证列表表示的数字不含前导零
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
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        flag = False
        while l1 or l2 or flag:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            v = v1 + v2 + 1 if flag else v1 + v2
            new_v = v - 10 if v >= 10 else v
            flag = True if v >= 10 else False

            node = ListNode(new_v)
            # print(node)
            curr.next = node
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        # print(dummy)
        return dummy.next


# @lc code=end


#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#
