from typing import List


class Solution:
    def perfectMenu(
        self,
        materials: List[int],
        cookbooks: List[List[int]],
        attribute: List[List[int]],
        limit: int,
    ) -> int:
        m = len(materials)
        n = len(cookbooks)
        # used = [False for _ in range(n)]
        sub_ans = []
        ans = []

        def dfs(idx):
            if idx >= n:
                ans.append(sub_ans[:])
                return

            dfs(idx + 1)

            sub_ans.append(idx)
            dfs(idx + 1)
            sub_ans.pop()

        dfs(0)

        def check_sub(sub):
            used = [0 for _ in range(m)]
            for i in sub_ans:
                for j, use in enumerate(cookbooks[i]):
                    used[j] += use
                    if used[j] > materials[j]:
                        return False

            return True

        res = -1

        for idx, sub_ans in enumerate(ans):
            if not len(sub_ans):
                continue

            x = 0
            y = 0

            if check_sub(sub_ans):
                print(sub_ans, "+++++++")
                for j in sub_ans:
                    x += attribute[j][0]
                    y += attribute[j][1]

                if y >= limit:
                    res = max(res, x)

        return res


s = Solution()
a = [3, 2, 4, 1, 2]
b = [[1, 1, 0, 1, 2], [2, 1, 4, 0, 0], [3, 2, 4, 1, 0]]
c = [[3, 2], [2, 4], [7, 6]]
d = 5
# a = [12, 13, 14, 15, 20]
# b = [[1, 1, 1, 1, 1], [3, 3, 3, 3, 3], [10, 10, 10, 10, 10]]
# c = [[5, 5], [6, 6], [10, 10]]
# d = 12
a = [10, 10, 10, 10, 10]
b = [[1, 1, 1, 1, 1], [3, 3, 3, 3, 3], [10, 10, 10, 10, 10]]
c = [[5, 5], [6, 6], [10, 10]]
d = 12


res = s.perfectMenu(a, b, c, d)
print(res)
