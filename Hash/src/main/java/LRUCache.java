// LRU缓存机制-146
// https://leetcode-cn.com/problems/lru-cache/

import java.util.HashMap;

public class LRUCache {
    int capacity;
    Node head;
    Node tail;

    class Node {
        int key;
        int value;
        Node next;
        Node pre;

    }

    HashMap<Integer, Node> map = new HashMap<>();

    public LRUCache(int capacity) {
        this.capacity = capacity;
        head = new Node();
        tail = new Node();
        head.next = tail;
        tail.pre = head;
    }

    public int get(int key) {
        if (!map.containsKey(key)) {
            return -1;
        }
        Node node = map.get(key);
        remove(node);
        insert(head, node);
        return node.value;
    }

    public void put(int key, int value) {
        if (!map.containsKey(key)) {
            Node newNode = new Node();
            newNode.value = value;
            newNode.key = key;
            insert(head, newNode);
            map.put(key, newNode);

            if (map.size() > capacity) {
                map.remove(tail.pre.key);
                remove(tail.pre);
            }
        } else {
            Node node = map.get(key);
            node.value = value;
            remove(node);
            insert(head, node);
        }
    }

    private void remove(Node node) {
        node.pre.next = node.next;
        node.next.pre = node.pre;
    }

    private void insert(Node from, Node node) {
        node.next = from.next;
        from.next.pre = node;
        // 这两组的顺序不能颠倒
        from.next = node;
        node.pre = from;
    }

    public static void main(String[] args) {
        LRUCache obj = new LRUCache(10);
        int param_1 = obj.get(1);
        System.out.println(param_1);
        obj.put(1, 100);
        obj.put(2, 100);
        obj.put(3, 100);
        obj.put(4, 100);
        obj.put(5, 100);
        obj.put(6, 100);
        obj.put(7, 100);
        obj.put(8, 100);
        obj.put(9, 100);
        obj.put(10, 100);
        obj.put(11, 100);
        obj.put(12, 100);
        obj.put(1, 100);
        obj.put(1, 100);
        obj.put(1, 100);
        obj.put(1, 100);
        System.out.println(obj.get(1));
    }

}
