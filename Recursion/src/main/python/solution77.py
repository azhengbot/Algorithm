from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n = n
        self.k = k
        self.sub_ans = []
        self.ans = []
        self.recur(1)
        return self.ans

    def recur(self, i):
        # if i == n:
        if i == self.n + 1:
            if len(self.sub_ans) == self.k:
                self.ans.append(self.sub_ans[:])
            return

        self.recur(i + 1)

        self.sub_ans.append(i)

        self.recur(i + 1)

        self.sub_ans.pop()


s = Solution()
res = s.combine(4, 2)
print(res)