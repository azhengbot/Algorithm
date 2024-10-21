#
# @lc app=leetcode.cn id=86 lang=python3
# @lcpr version=30204
#
# [86] 分隔链表
#
# https://leetcode.cn/problems/partition-list/description/
#
# algorithms
# Medium (65.14%)
# Likes:    862
# Dislikes: 0
# Total Accepted:    311.8K
# Total Submissions: 478.2K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
#
# 你应当 保留 两个分区中每个节点的初始相对位置。
#
#
#
# 示例 1：
#
# 输入：head = [1,4,3,2,5,2], x = 3
# 输出：[1,2,2,4,3,5]
#
#
# 示例 2：
#
# 输入：head = [2,1], x = 2
# 输出：[1,2]
#
#
#
#
# 提示：
#
#
# 链表中节点的数目在范围 [0, 200] 内
# -100 <= Node.val <= 100
# -200 <= x <= 200
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode()
        big = ListNode()

        dummy_small = small
        dummy_big = big

        curr = head

        while curr:
            # print(curr)
            if curr.val < x:
                small.next = curr
                small = small.next
            else:
                big.next = curr
                big = big.next

            _next = curr.next
            curr.next = None
            curr = _next

        small.next = dummy_big.next
        return dummy_small.next


# @lc code=end


#
# @lcpr case=start
# [1,4,3,2,5,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n
# @lcpr case=end

#
