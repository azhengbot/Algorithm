#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (56.55%)
# Likes:    1875
# Dislikes: 0
# Total Accepted:    437.3K
# Total Submissions: 770.2K
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

from collections import defaultdict
from heapq import heappop, heappush

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = []
        dic = defaultdict(list)
        dummy = ListNode()
        cur = dummy
        if not lists:
            return None
        
        for node in lists:
            if node:
                dic[node.val].append(node)
                heappush(hq, node.val)

        while hq:
            val = heappop(hq)
            head_list = dic[val]
            head = head_list.pop()
            cur.next = head
            cur = cur.next
            if head.next:
                next_val = head.next.val
                heappush(hq, next_val)
                dic[next_val].append(head.next)

        return dummy.next
    


    

# @lc code=end

