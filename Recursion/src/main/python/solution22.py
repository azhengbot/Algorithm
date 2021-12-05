from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]

        ans = []

        for i in range(n):
            first_part = self.generateParenthesis(i)
            second_part = self.generateParenthesis(n - i - 1)

            for fp in first_part:
                for sp in second_part:
                    res = f"({fp}){sp}"
                    ans.append(res)

        return ans


s = Solution()
res = s.generateParenthesis(3)
print(res)
