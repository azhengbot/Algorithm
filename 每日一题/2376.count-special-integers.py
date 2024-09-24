#
# @lc app=leetcode.cn id=2376 lang=python3
# @lcpr version=30204
#
# [2376] 统计特殊整数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)

        @cache
        def dfs(i, mask, is_limit, is_num):
            if i == len(s):
                return 1 if is_num else 0
            res = 0
            if not is_num:
                res = dfs(i + 1, mask, False, False)

            low = 0 if is_num else 1
            up = int(s[i]) if is_limit else 9

            for d in range(low, up + 1):
                if mask >> d & 1 == 0:
                    res += dfs(i + 1, mask | (1 << d), is_limit and d == up, True)

            return res

        return dfs(0, 0, True, False)


# @lc code=end


#
# @lcpr case=start
# 20\n
# @lcpr case=end

# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 135\n
# @lcpr case=end

#
