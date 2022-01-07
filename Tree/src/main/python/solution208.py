class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        self.find(word, True, False)

    def search(self, word: str) -> bool:
        return self.find(word, False, False)

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix, False, True)

    def find(self, word, is_insert, is_prefix):
        cur = self.root
        for w in word:
            if not cur.child[ord(w) - ord("a")]:  # type: ignore
                if is_insert:
                    cur.child[ord(w) - ord("a")] = Node()  # type: ignore
                else:
                    return False
            cur = cur.child[ord(w) - ord("a")]  # type: ignore
        if is_insert:
            cur.count += 1  # type: ignore
        if is_prefix:
            return True
        return cur.count > 0  # type: ignore


class Node:
    def __init__(self):
        self.count = 0
        self.child = [None for _ in range(26)]


# Your Trie object will be instantiated and called as such:
word = "abcd"
prefix = "ab"
# word = ""
# prefix = "a"
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)

print(param_3)
