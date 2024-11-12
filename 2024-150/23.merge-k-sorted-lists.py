#
# @lc app=leetcode.cn id=23 lang=python3
# @lcpr version=30204
#
# [23] 合并 K 个升序链表
#
# https://leetcode.cn/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (60.71%)
# Likes:    2909
# Dislikes: 0
# Total Accepted:    893.5K
# Total Submissions: 1.5M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 给你一个链表数组，每个链表都已经按升序排列。
# 
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
# 
# 
# 
# 示例 1：
# 
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
# 
# 
# 示例 2：
# 
# 输入：lists = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 输入：lists = [[]]
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4
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
from typing import List, Optional
from heapq import heapify, heapreplace, heappush, heappop

class Node:
    def __init__(self, val, node) -> None:
        self.val = val    
        self.node = node
    
    def __lt__(self, value: object) -> bool:
        return self.val < value.val
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = []

        for node in lists:
            if node:
                heappush(hq, Node(node.val, node))

        dummy = ListNode()
        curr = dummy

        while hq:
            # print(hq)
            n = heappop(hq)
            node = n.node

            curr.next = node
            curr = curr.next
            if node.next:
                heappush(hq, Node(node.next.val, node.next))
                
        return dummy.next
# @lc code=end



#
# @lcpr case=start
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [[]]\n
# @lcpr case=end

#

