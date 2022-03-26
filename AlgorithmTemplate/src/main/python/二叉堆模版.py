#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (56.52%)
# Likes:    1775
# Dislikes: 0
# Total Accepted:    403.3K
# Total Submissions: 713.2K
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

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List, Optional


class BinaryHeap:
    def __init__(self) -> None:
        # 0 位不算，下标从 1 开始，
        # 满足根节点下标 i 与叶子节点下标为 2i 和 2i + 1 的关系
        self.heap = [0]

    def is_empty(self):
        return len(self.heap) <= 1

    def push_(self, node: ListNode):
        # 插入到尾部
        self.heap.append(node)
        # 向上调整
        self.heapify_up(len(self.heap) - 1)
        # print([i.val for i in self.heap[1:]])

    def pop_(self):
        ans = self.heap[1]
        # 末尾交换到头部，然后删除末尾
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        # 向下调整
        self.heapify_down(1)
        return ans

    def heapify_up(self, leaf):
        while leaf > 1:
            root = leaf // 2
            # print(self.heap[leaf], leaf)
            if self.heap[leaf].val < self.heap[root].val:  # 小根堆
                self.heap[root], self.heap[leaf] = self.heap[leaf], self.heap[root]
                leaf = root
            else:
                break

    def heapify_down(self, root):
        child = 2 * root

        while child < len(self.heap):  # child未出界，说明p有合法的child，还不是叶子
            other_child = 2 * root + 1
            # 先比较两个孩子，谁小就继续跟p比较
            # child存较小的孩子
            if (
                other_child < len(self.heap)
                and self.heap[other_child].val < self.heap[child].val
            ):
                child = other_child
            # 让 child 跟 root 比较
            if self.heap[root].val > self.heap[child].val:
                self.heap[root], self.heap[child] = self.heap[child], self.heap[root]
                root = child
                child = 2 * root
            else:
                break


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        bh = BinaryHeap()

        for node in lists:
            if node:
                bh.push_(node)
        head = ListNode()
        curr = head

        while not bh.is_empty():

            node = bh.pop_()
            node_next = node.next

            if node_next:
                bh.push_(node_next)

            curr.next = node
            curr = curr.next

        return head.next


# @lc code=end
