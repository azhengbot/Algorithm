class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        self.find(word, True, False)

    def search(self, word: str) -> bool:
        return self.find(word, False, False)

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix, False, True)

    def find(self, s: str, is_insert: bool, is_prefix: bool) -> bool:
        cur = self.root

        for char in s:
            if not cur.child.get(char):
                if is_insert:
                    cur.child[char] = Node()
                else:
                    return False

            cur = cur.child[char]

        if is_insert:
            cur.count += 1
        if is_prefix:
            return True

        return cur.count > 0


class Node:
    def __init__(self) -> None:
        self.count = 0
        self.child = {}


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
