#
# @lc app=leetcode.cn id=715 lang=python3
#
# [715] Range 模块
#
# https://leetcode-cn.com/problems/range-module/description/
#
# algorithms
# Hard (41.84%)
# Likes:    160
# Dislikes: 0
# Total Accepted:    11.8K
# Total Submissions: 22.8K
# Testcase Example:  '["RangeModule","addRange","removeRange","queryRange","queryRange","queryRange"]\n' +
  '[[],[10,20],[14,16],[10,14],[13,15],[16,17]]'
#
# Range模块是跟踪数字范围的模块。设计一个数据结构来跟踪表示为 半开区间 的范围并查询它们。
# 
# 半开区间 [left, right) 表示所有 left <= x < right 的实数 x 。
# 
# 实现 RangeModule 类:
# 
# 
# RangeModule() 初始化数据结构的对象。
# void addRange(int left, int right) 添加 半开区间 [left,
# right)，跟踪该区间中的每个实数。添加与当前跟踪的数字部分重叠的区间时，应当添加在区间 [left, right)
# 中尚未跟踪的任何数字到该区间中。
# boolean queryRange(int left, int right) 只有在当前正在跟踪区间 [left, right)
# 中的每一个实数时，才返回 true ，否则返回 false 。
# void removeRange(int left, int right) 停止跟踪 半开区间 [left, right)
# 中当前正在跟踪的每个实数。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入
# ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange",
# "queryRange"]
# [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
# 输出
# [null, null, null, true, false, true]
# 
# 解释
# RangeModule rangeModule = new RangeModule();
# rangeModule.addRange(10, 20);
# rangeModule.removeRange(14, 16);
# rangeModule.queryRange(10, 14); 返回 true （区间 [10, 14) 中的每个数都正在被跟踪）
# rangeModule.queryRange(13, 15); 返回 false（未跟踪区间 [13, 15) 中像 14, 14.03, 14.17
# 这样的数字）
# rangeModule.queryRange(16, 17); 返回 true （尽管执行了删除操作，区间 [16, 17) 中的数字 16
# 仍然会被跟踪）
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= left < right <= 10^9
# 在单个测试用例中，对 addRange 、  queryRange 和 removeRange 的调用总数不超过 10^4 次
# 
# 
#

# @lc code=start
class RangeModule:
    def __init__(self):
        self.root = SegmentTree()

    def addRange(self, left: int, right: int) -> None:
        self.root.update(left, right - 1, 1)

    def queryRange(self, left: int, right: int) -> bool:
        return self.root.query(left, right - 1)

    def removeRange(self, left: int, right: int) -> None:
        self.root.update(left, right - 1, -1)


class Node:
    def __init__(self, l, r):
        self.left = None
        self.right = None
        self.l = l
        self.r = r
        self.mid = (l + r) // 2
        self.val = False
        self.add = 0


class SegmentTree:
    def __init__(self):
        self.root = Node(1, int(1e9))

    def pushdown(self, node):
        if not node.left:
            node.left = Node(node.l, node.mid)
        if not node.right:
            node.right = Node(node.mid + 1, node.r)

        if node.add == 0:
            return

        node.left.add = node.add
        node.left.val = node.add == 1
        node.right.add = node.add
        node.right.val = node.add == 1
        node.add = 0

    def pushup(self, node):
        node.val = node.left.val and node.right.val

    def update(self, l, r, val, node=None):

        if not node:
            node = self.root

        if l <= node.l and node.r <= r:
            node.val = val == 1
            node.add = val
            return

        self.pushdown(node)

        if l <= node.mid:
            self.update(l, r, val, node.left)

        if r > node.mid:
            self.update(l, r, val, node.right)

        self.pushup(node)

    def query(self, l, r, node=None):
        if not node:
            node = self.root
        # print(l, r, node.l, node.r, node.val)

        if l <= node.l and node.r <= r:
            return node.val

        self.pushdown(node)

        res = True

        if l <= node.mid:
            res = res and self.query(l, r, node.left)
            # print(l, r, res, node.l, node.r, node.val, "++++++")
        if r > node.mid:
            res = res and self.query(l, r, node.right)
            # print(l, r, res, node.l, node.r, node.val, "-----")

        # print(l, r, node.l, node.r, res, "*********")
        return res



# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
# @lc code=end

