"""
如果一个正整数每一个数位都是 互不相同 的，我们称它是 特殊整数 。
给你一个 正 整数 n ，请你返回区间 [1, n] 之间特殊整数的数目。
"""

from functools import lru_cache


class Solution:
    def countSpecialNumbers(self, n: int) -> int:

        s = str(n)

        # @lru_cache()
        def f(idx: int, mask: int, is_limit: bool, is_num: bool):
            if idx == len(s):
                return int(is_num)

            res = 0
            if not is_num:
                res = f(idx + 1, mask, False, False)

            up = int(s[idx]) if is_limit else 9
            if is_num:
                low = 0
            else:
                low = 1

            for d in range(low, up + 1):
                if mask >> d & 1 == 0:
                    res += f(idx + 1, mask | (1 << d), is_limit and d == up, True)

            return res

        return f(0, 0, True, False)


s = Solution()

res = s.countSpecialNumbers(20)
print(res)
