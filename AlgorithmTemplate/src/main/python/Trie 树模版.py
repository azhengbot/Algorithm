#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#
# https://leetcode-cn.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (71.89%)
# Likes:    1112
# Dislikes: 0
# Total Accepted:    180.5K
# Total Submissions: 251.2K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Trie（发音类似 "try"）或者说 前缀树
# 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
#
# 请你实现 Trie 类：
#
#
# Trie() 初始化前缀树对象。
# void insert(String word) 向前缀树中插入字符串 word 。
# boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false
# 。
# boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true
# ；否则，返回 false 。
#
#
#
#
# 示例：
#
#
# 输入
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# 输出
# [null, null, true, false, true, null, true]
#
# 解释
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // 返回 True
# trie.search("app");     // 返回 False
# trie.startsWith("app"); // 返回 True
# trie.insert("app");
# trie.search("app");     // 返回 True
#
#
#
#
# 提示：
#
#
# 1
# word 和 prefix 仅由小写英文字母组成
# insert、search 和 startsWith 调用次数 总计 不超过 3 * 10^4 次
#
#
#

# @lc code=start

# 列表形式
# class Trie:
#     def __init__(self):
#         self.root = [0, [[] for _ in range(26)]]

#     def insert(self, word: str) -> None:
#         self.find(word, is_insert=True)

#     def search(self, word: str) -> bool:
#         return self.find(word)

#     def startsWith(self, prefix: str) -> bool:
#         return self.find(prefix, is_prefix=True)

#     def find(self, word: str, is_insert=False, is_prefix=False):
#         curr = self.root
#         for c in word:
#             if not curr[1][ord(c) - ord("a")]:
#                 if is_insert:
#                     curr[1][ord(c) - ord("a")] = [0, [[] for _ in range(26)]]
#                 else:
#                     return False

#             curr = curr[1][ord(c) - ord("a")]

#         if is_insert:
#             curr[0] += 1

#         if is_prefix:
#             return True

#         return curr[0] > 0

# 字典形式
class Trie:
    def __init__(self):
        self.root = [0, {}]

    def insert(self, word: str) -> None:
        self.find(word, is_insert=True)

    def search(self, word: str) -> bool:
        return self.find(word)

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix, is_prefix=True)

    def find(self, word: str, is_insert=False, is_prefix=False):
        curr = self.root
        for c in word:
            if not curr[1].get(c):
                if is_insert:
                    curr[1][c] = [0, {}]
                else:
                    return False

            curr = curr[1][c]

        if is_insert:
            curr[0] += 1

        if is_prefix:
            return True

        return curr[0] > 0


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
