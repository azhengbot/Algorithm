from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)

        self.fa = [i for i in range(n)]

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    self.union_set(i, j)

        ans = 0

        for i in range(n):
            if self.find(i) == i:
                ans += 1

        return ans

    def find(self, x):
        if x == self.fa[x]:
            return x

        self.fa[x] = self.find(self.fa[x])

        return self.fa[x]

    def union_set(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x != y:
            self.fa[x] = y


s = Solution()
isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
res = s.findCircleNum(isConnected)
print(res)

fa = [0, 1, 1, 2, 3, 4]


def test_find(x):

    if x == fa[x]:
        return x

    fa[x] = test_find(fa[x])

    print(fa)
    return fa[x]


print(test_find(5))
