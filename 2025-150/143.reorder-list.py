#
# @lc app=leetcode.cn id=143 lang=python3
# @lcpr version=30204
#
# [143] 重排链表
#
# https://leetcode.cn/problems/reorder-list/description/
#
# algorithms
# Medium (67.11%)
# Likes:    1568
# Dislikes: 0
# Total Accepted:    359.5K
# Total Submissions: 535.7K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
#
# L0 → L1 → … → Ln - 1 → Ln
#
#
# 请将其重新排列后变为：
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# 示例 1：
#
#
#
# 输入：head = [1,2,3,4]
# 输出：[1,4,2,3]
#
# 示例 2：
#
#
#
# 输入：head = [1,2,3,4,5]
# 输出：[1,5,2,4,3]
#
#
#
# 提示：
#
#
# 链表的长度范围为 [1, 5 * 10^4]
# 1 <= node.val <= 1000
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
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        n = 0
        idx_map = dict()

        while curr:
            idx_map[n] = curr
            curr = curr.next
            n += 1

        for i in range(n // 2):
            tail_node = idx_map[n - i - 1]
            idx_map[n - i - 2].next = None
            head = idx_map[i]
            nxt = head.next

            head.next = tail_node
            tail_node.next = nxt


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#
