#
# @lc app=leetcode.cn id=127 lang=python3
# @lcpr version=30204
#
# [127] 单词接龙
#
# https://leetcode.cn/problems/word-ladder/description/
#
# algorithms
# Hard (49.22%)
# Likes:    1420
# Dislikes: 0
# Total Accepted:    233.4K
# Total Submissions: 474K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 字典 wordList 中从单词 beginWord 到 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 ->
# s2 -> ... -> sk：
# 
# 
# 每一对相邻的单词只差一个字母。
# 对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
# sk == endWord
# 
# 
# 给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列
# 中的 单词数目 。如果不存在这样的转换序列，返回 0 。
# 
# 
# 示例 1：
# 
# 输入：beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# 输出：5
# 解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
# 
# 
# 示例 2：
# 
# 输入：beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# 输出：0
# 解释：endWord "cog" 不在字典中，所以无法进行转换。
# 
# 
# 
# 提示：
# 
# 
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord、endWord 和 wordList[i] 由小写英文字母组成
# beginWord != endWord
# wordList 中的所有字符串 互不相同
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict, deque
class Solution:
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_id = dict() 
        graph = defaultdict(list)
        node_id = 1
        if endWord not in wordList:
            return 0
        def add_word(word):
            nonlocal node_id
            if word not in word_id:
                word_id[word] = node_id
                node_id += 1


        def add_edge(word):
            add_word(word)
            id1 = word_id[word]
            char_list = list(word)
            n = len(char_list)
            for i in range(n):
                tmp_char = char_list[i]
                char_list[i] = "*"
                word2 = "".join(char_list)
                add_word(word2)
                id2 = word_id[word2]
                graph[id1].append(id2)
                graph[id2].append(id1)
                char_list[i] = tmp_char

        for word in wordList:
            add_edge(word)
        add_edge(beginWord)
        # add_edge(endWord)

        dq = deque([word_id[beginWord]])
        ans = [float("inf")] * node_id
        ans[word_id[beginWord]] = 0
        
        while dq:
            wid = dq.popleft()
            if wid  == word_id[endWord]:
                return ans[wid] // 2 + 1
            
            for nxt in graph[wid]:
                if ans[nxt] == float("inf"):
                    dq.append(nxt)
                    ans[nxt] = ans[wid] + 1
        return 0

            

# @lc code=end



#
# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]\n
# @lcpr case=end

# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log"]\n
# @lcpr case=end

#

