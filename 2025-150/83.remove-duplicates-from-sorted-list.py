#
# @lc app=leetcode.cn id=83 lang=python3
# @lcpr version=30204
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (54.27%)
# Likes:    1178
# Dislikes: 0
# Total Accepted:    750.4K
# Total Submissions: 1.4M
# Testcase Example:  '[1,1,2]'
#
# 给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
#
#
#
# 示例 1：
#
# 输入：head = [1,1,2]
# 输出：[1,2]
#
#
# 示例 2：
#
# 输入：head = [1,1,2,3,3]
# 输出：[1,2,3]
#
#
#
#
# 提示：
#
#
# 链表中节点数目在范围 [0, 300] 内
# -100 <= Node.val <= 100
# 题目数据保证链表已经按升序 排列
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:


# @lc code=end


#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3,3]\n
# @lcpr case=end

#
