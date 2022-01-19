from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        sub_ans = []
        ans = []
        left_count = n
        right_count = n

        def dfs(idx):
            nonlocal left_count, right_count
            if idx >= 2 * n:
                if check(sub_ans):
                    ans.append("".join(sub_ans))
                return

            if left_count > 0:
                sub_ans.append("(")
                left_count -= 1
                dfs(idx + 1)
                sub_ans.pop()
                left_count += 1

            if right_count > 0:
                sub_ans.append(")")
                right_count -= 1
                dfs(idx + 1)
                sub_ans.pop()
                right_count += 1

        def check(l):
            stack = []
            for i in l:
                if len(stack) == 0 or i == "(":
                    stack.append(i)
                    continue
                if i == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False

            return len(stack) == 0

        dfs(0)
        return ans
