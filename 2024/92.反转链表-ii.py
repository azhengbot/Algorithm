#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode.cn/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (55.89%)
# Likes:    1728
# Dislikes: 0
# Total Accepted:    467K
# Total Submissions: 835.2K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left  。请你反转从位置 left 到位置 right 的链表节点，返回
# 反转后的链表 。
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点数目为 n
# 1 
# -500 
# 1 
# 
# 
# 
# 
# 进阶： 你可以使用一趟扫描完成反转吗？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        start_before = None
        start_node = None
        end_after = None
        end_node = None

        node = ListNode()
        node.next = head
        dummy = node
        if left == right:
            return head
        cnt = 0

        while node:
            # print(dummy)
            # print(node)
            if not node:
                return

            if cnt + 1 == left:
                start_before = node
                node = node.next
                # print(start_before, "&&&&")
            elif cnt == left:
                start_node = node
                old_node = node
                node = node.next

            elif start_node and not end_node:
                if cnt == right:
                    end_node =node
                    end_after = node.next
                # print(old_node)
                nex = node.next
                # if old_node.next == old_node:
                if old_node == start_node:
                    old_node.next = None
                # old_node.next = None
                node.next = old_node
                old_node = node
                # print(start_before, "------", node)
                node = nex
            
            elif node:
                node = node.next
            
            cnt += 1

            # print("--------")


            
        # print(start_before, "*****")
        start_before.next = end_node
        start_node.next = end_after

        return dummy.next

                


            


# @lc code=end

