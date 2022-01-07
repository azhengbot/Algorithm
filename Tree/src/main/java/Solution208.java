import java.util.HashMap;

class Trie {

    class Node {
        HashMap<Character, Node> child;
        int count;

        public Node() {
            count = 0;
            child = new HashMap<>();
        }
    }

    Node root;

    public Trie() {
        this.root = new Node();
    }

    public void insert(String word) {
        find(word, true, false);
    }

    public boolean search(String word) {
        return find(word, false, false);
    }

    public boolean startsWith(String prefix) {
        return find(prefix, false, true);
    }

    private boolean find(String s, boolean isInsert, boolean isPrefix) {
        Node cur = root;

        for (char ch : s.toCharArray()) {
            if (!cur.child.containsKey(ch)) {
                if (isInsert) {
                    cur.child.put(ch, new Node());
                } else {
                    return false;
                }
            }
            cur = cur.child.get(ch);
        }

        if (isInsert)
            cur.count++;
        if (isPrefix)
            return true;

        return cur.count > 0;
    }
}

public class Solution208 {
    public static void main(String[] args) {
        String word = "application";
        String prefix = "app";
        Trie obj = new Trie();
        obj.insert(word);
        boolean param_2 = obj.search(word);
        boolean param_3 = obj.startsWith(prefix);

        System.out.println(param_2);
        System.out.println(param_3);
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */