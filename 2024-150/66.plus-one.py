#
# @lc app=leetcode.cn id=66 lang=python3
# @lcpr version=30204
#
# [66] 加一
#
# https://leetcode.cn/problems/plus-one/description/
#
# algorithms
# Easy (46.25%)
# Likes:    1447
# Dislikes: 0
# Total Accepted:    794K
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,3]'
#
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
#
#
# 示例 1：
#
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
#
#
# 示例 2：
#
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
#
#
# 示例 3：
#
# 输入：digits = [9]
# 输出：[1,0]
# 解释：输入数组表示数字 9。
# 加 1 得到了 9 + 1 = 10。
# 因此，结果应该是 [1,0]。
#
#
#
#
# 提示：
#
#
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = 0

        n = len(digits)
        ans = []
        for i in range(n - 1, -1, -1):
            d = digits[i]
            if i == n - 1 or flag:
                d += 1
                if d >= 10:
                    flag = 1
                    ans.insert(0, d - 10)
                else:
                    flag = 0
                    ans.insert(0, d)
            else:
                flag = 0
                ans.insert(0, d)
        if flag:
            ans.insert(0, 1)
        return ans


# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [9]\n
# @lcpr case=end

#
