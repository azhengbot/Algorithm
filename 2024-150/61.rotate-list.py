#
# @lc app=leetcode.cn id=61 lang=python3
# @lcpr version=30204
#
# [61] 旋转链表
#
# https://leetcode.cn/problems/rotate-list/description/
#
# algorithms
# Medium (41.45%)
# Likes:    1100
# Dislikes: 0
# Total Accepted:    422.1K
# Total Submissions: 1M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
#
#
#
# 示例 1：
#
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
#
#
# 示例 2：
#
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]
#
#
#
#
# 提示：
#
#
# 链表中节点的数目在范围 [0, 500] 内
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 10^9
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        lst = []
        back = head

        while back:
            lst.append(back)
            back = back.next

        n = len(lst)
        k = k % n

        if k == 0:
            return head

        lst[-k - 1].next = None

        lst[-1].next = head

        return lst[-k]


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2]\n4\n
# @lcpr case=end

#
