from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        used_col = [False for _ in range(n)]
        # 判断是否在对角线， 也要存一下
        used_plus = {}
        used_minus = {}
        res = []
        ans = []
        row = col = n

        def dfs(pos):
            nonlocal row, col, res, ans
            if pos == row:
                ans.append(res[:])
                return

            for i in range(col):
                if used_col[i] or used_plus.get(pos + i) or used_minus.get(pos - i):
                    continue
                used_col[i] = True
                used_plus[pos + i] = True
                used_minus[pos - i] = True
                res.append(i)
                dfs(pos + 1)
                res.pop()
                used_minus[pos - i] = False
                used_plus[pos + i] = False
                used_col[i] = False

        dfs(0)

        fina_res = []
        # 将位置信息拼接成最终答案
        for i in range(len(ans)):
            res = ans[i]
            res_lst = [["." for _ in range(n)] for _ in range(n)]
            for idx, j in enumerate(res):
                res_lst[idx][j] = "Q"

            # final_res_str = "".join(res_str)
            res = []
            for l in res_lst:
                res.append("".join(l))

            fina_res.append(res)
        return fina_res


s = Solution()
n = 4
res = s.solveNQueens(n)

print(res)