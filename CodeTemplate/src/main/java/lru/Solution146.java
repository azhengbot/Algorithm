package lru;

import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=146 lang=java
 *
 * [146] LRU 缓存
 *
 * https://leetcode-cn.com/problems/lru-cache/description/
 *
 * algorithms
 * Medium (52.49%)
 * Likes:    1943
 * Dislikes: 0
 * Total Accepted:    289.4K
 * Total Submissions: 551K
 * Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
 *
 * 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
 * 
 * 实现 LRUCache 类：
 * 
 * 
 * 
 * 
 * LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
 * int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
 * void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组
 * key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
 * 
 * 
 * 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
 * 
 * 
 * 
 * 
 * 
 * 示例：
 * 
 * 
 * 输入
 * ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
 * [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
 * 输出
 * [null, null, null, 1, null, -1, null, -1, 3, 4]
 * 
 * 解释
 * LRUCache lRUCache = new LRUCache(2);
 * lRUCache.put(1, 1); // 缓存是 {1=1}
 * lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
 * lRUCache.get(1);    // 返回 1
 * lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
 * lRUCache.get(2);    // 返回 -1 (未找到)
 * lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
 * lRUCache.get(1);    // 返回 -1 (未找到)
 * lRUCache.get(3);    // 返回 3
 * lRUCache.get(4);    // 返回 4
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= capacity <= 3000
 * 0 <= key <= 10000
 * 0 <= value <= 10^5
 * 最多调用 2 * 10^5 次 get 和 put
 * 
 * 
 */

// @lc code=start
class LRUCache {
    private int capacity;
    private HashMap<Integer, Node> map;
    private Node head;
    private Node tail;

    class Node {
        public int key;
        public int value;
        // 保护节点
        public Node pre;
        public Node next;
    }

    public LRUCache(int capacity) {
        this.capacity = capacity;
        // 建立带有保护结点的空双向链表
        this.head = new Node();
        this.tail = new Node();
        this.map = new HashMap<>();

        head.next = tail;
        tail.pre = head;

    }

    public int get(int key) {
        if (!map.containsKey(key)) {
            return -1;
        }
        Node node = map.get(key);
        // 从链表中删除
        removeNode(node);
        // 放到链表头部， 维护时间顺序
        insertNode(head, node);

        return node.value;
    }

    public void put(int key, int value) {
        if (map.containsKey(key)) {
            Node node = map.get(key);
            // 从链表中删除
            removeNode(node);
            // 更新 value， 插入链表头部
            node.value = value;
            insertNode(head, node);

        } else {
            // 在链表中插入新节点
            Node node = new Node();
            node.key = key;
            node.value = value;
            insertNode(head, node);
            map.put(key, node);
        }
        // 超过最大值，需要删除尾部节点，并移除 map 的值
        if (map.size() > capacity) {
            Node node = tail.pre;
            removeNode(node);
            map.remove(node.key);
        }

    }

    private void insertNode(Node preNode, Node node) {
        node.next = preNode.next;
        node.pre = preNode;
        preNode.next.pre = node;
        preNode.next = node;
    }

    private void removeNode(Node node) {
        node.next.pre = node.pre;
        node.pre.next = node.next;
    }

    public static void main(String[] args) {
        LRUCache obj = new LRUCache(2);
        obj.put(1, 1);
        obj.put(2, 2);
        int param_1 = obj.get(1);
        obj.put(3, 3);
        int param_2 = obj.get(2);

        System.out.println(param_1);
        System.out.println(param_2);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
// @lc code=end
