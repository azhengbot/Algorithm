#
# @lc app=leetcode.cn id=1073 lang=python3
#
# [1073] 负二进制数相加
#
# https://leetcode.cn/problems/adding-two-negabinary-numbers/description/
#
# algorithms
# Medium (35.42%)
# Likes:    102
# Dislikes: 0
# Total Accepted:    11.1K
# Total Submissions: 27.5K
# Testcase Example:  '[1,1,1,1,1]\n[1,0,1]'
#
# 给出基数为 -2 的两个数 arr1 和 arr2，返回两数相加的结果。
#
# 数字以 数组形式 给出：数组由若干 0 和 1 组成，按最高有效位到最低有效位的顺序排列。例如，arr = [1,1,0,1] 表示数字 (-2)^3 +
# (-2)^2 + (-2)^0 = -3。数组形式 中的数字 arr 也同样不含前导零：即 arr == [0] 或 arr[0] == 1。
#
# 返回相同表示形式的 arr1 和 arr2 相加的结果。两数的表示形式为：不含前导零、由若干 0 和 1 组成的数组。
#
#
#
# 示例 1：
#
#
# 输入：arr1 = [1,1,1,1,1], arr2 = [1,0,1]
# 输出：[1,0,0,0,0]
# 解释：arr1 表示 11，arr2 表示 5，输出表示 16 。
#
#
#
#
# 示例 2：
#
#
# 输入：arr1 = [0], arr2 = [0]
# 输出：[0]
#
#
# 示例 3：
#
#
# 输入：arr1 = [0], arr2 = [1]
# 输出：[1]
#
#
#
#
# 提示：
#
#
#
# 1 <= arr1.length, arr2.length <= 1000
# arr1[i] 和 arr2[i] 都是 0 或 1
# arr1 和 arr2 都没有前导0
#
#
#

# @lc code=start
from typing import List


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a1 = sum([(-2) ** (len(arr1) - 1 - i) for i, ar in enumerate(arr1) if ar != 0])
        a2 = sum([(-2) ** (len(arr2) - 1 - i) for i, ar in enumerate(arr2) if ar != 0])
        # print([(-(2**i)) for i, ar in enumerate(arr1) if ar != 0])
        # print(a1, a2)
        res = a1 + a2
        ans = []

        while res != 0:
            # print(res, "+++")
            if res > 0:
                if res == 1:
                    t = 1
                else:
                    t = abs(res) % 2
                res = -(res // 2)
            else:
                t = abs(res) % 2
                res = -res // 2 + 1 if t else (-res // 2)
            ans.append(t)
        if not ans:
            return [0]
        return list(reversed(ans))


# @lc code=end

s = Solution()
arr1 = [1, 1, 1, 1, 1]
arr2 = [1, 0, 1]
res = s.addNegabinary(arr1, arr2)
print(res)
