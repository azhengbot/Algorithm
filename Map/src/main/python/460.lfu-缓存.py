#
# @lc app=leetcode.cn id=460 lang=python3
#
# [460] LFU 缓存
#
# https://leetcode.cn/problems/lfu-cache/description/
#
# algorithms
# Hard (45.08%)
# Likes:    708
# Dislikes: 0
# Total Accepted:    69.8K
# Total Submissions: 152.8K
# Testcase Example:  '["LFUCache","put","put","get","put","get","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]'
#
# 请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。
#
# 实现 LFUCache 类：
#
#
# LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象
# int get(int key) - 如果键 key 存在于缓存中，则获取键的值，否则返回 -1 。
# void put(int key, int value) - 如果键 key 已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量
# capacity 时，则应该在插入新项之前，移除最不经常使用的项。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最近最久未使用
# 的键。
#
#
# 为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。
#
# 当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put 操作，使用计数器的值将会递增。
#
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
#
#
#
# 示例：
#
#
# 输入：
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get",
# "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# 输出：
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
#
# 解释：
# // cnt(x) = 键 x 的使用计数
# // cache=[] 将显示最后一次使用的顺序（最左边的元素是最近的）
# LFUCache lfu = new LFUCache(2);
# lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
# lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lfu.get(1);      // 返回 1
# ⁠                // cache=[1,2], cnt(2)=1, cnt(1)=2
# lfu.put(3, 3);   // 去除键 2 ，因为 cnt(2)=1 ，使用计数最小
# ⁠                // cache=[3,1], cnt(3)=1, cnt(1)=2
# lfu.get(2);      // 返回 -1（未找到）
# lfu.get(3);      // 返回 3
# ⁠                // cache=[3,1], cnt(3)=2, cnt(1)=2
# lfu.put(4, 4);   // 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
# ⁠                // cache=[4,3], cnt(4)=1, cnt(3)=2
# lfu.get(1);      // 返回 -1（未找到）
# lfu.get(3);      // 返回 3
# ⁠                // cache=[3,4], cnt(4)=1, cnt(3)=3
# lfu.get(4);      // 返回 4
# ⁠                // cache=[3,4], cnt(4)=2, cnt(3)=3
#
#
#
# 提示：
#
#
# 1 <= capacity <= 10^4
# 0 <= key <= 10^5
# 0 <= value <= 10^9
# 最多调用 2 * 10^5 次 get 和 put 方法
#
#
#

# @lc code=start
from collections import defaultdict


class Node:
    __slots__ = ["key", "val", "cnt", "prev", "next_"]

    def __init__(self, key=0, val=0) -> None:
        self.key = key
        self.val = val
        self.cnt = 1


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}

        def new_dummy():
            dummy = Node()
            dummy.next_ = dummy
            dummy.prev = dummy
            return dummy

        self.cnt_to_node = defaultdict(new_dummy)

    def remove(self, node):
        node.next_.prev = node.prev
        node.prev.next_ = node.next_

    def push_to_fronted(self, dummy, node):
        # node.next_ = fronted
        # node.prev = fronted.prev
        # fronted.prev.next_ = node
        # fronted.prev = node
        node.prev = dummy
        node.next_ = dummy.next_
        node.prev.next_ = node
        node.next_.prev = node

    def get_node(self, key: int):
        if not self.key_to_node.get(key):
            return None
        node = self.key_to_node[key]
        self.remove(node)

        cnt = node.cnt
        dummy = self.cnt_to_node[cnt]

        if dummy.prev == dummy:
            del self.cnt_to_node[cnt]
            if self.min_cnt == cnt:
                self.min_cnt += 1
        node.cnt += 1
        self.push_to_fronted(self.cnt_to_node[cnt + 1], node)

        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.val if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.val = value
            return

        # dummy = self.cnt_to_node[1]
        # node = Node(key=key, val=value)

        if len(self.key_to_node) >= self.capacity:
            dummy = self.cnt_to_node[self.min_cnt]
            back_node = dummy.prev
            del self.key_to_node[back_node.key]
            self.remove(back_node)
            if dummy.prev == dummy:
                del self.cnt_to_node[self.min_cnt]

        self.key_to_node[key] = node = Node(key=key, val=value)
        self.push_to_fronted(self.cnt_to_node[1], node)
        self.min_cnt = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
