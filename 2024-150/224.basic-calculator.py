# @lcpr-before-debug-begin

# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=224 lang=python3
# @lcpr version=30204
#
# [224] 基本计算器
#
# https://leetcode.cn/problems/basic-calculator/description/
#
# algorithms
# Hard (43.11%)
# Likes:    1090
# Dislikes: 0
# Total Accepted:    164.1K
# Total Submissions: 380.7K
# Testcase Example:  '"1 + 1"'
#
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
#
# 注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。
#
#
#
# 示例 1：
#
# 输入：s = "1 + 1"
# 输出：2
#
#
# 示例 2：
#
# 输入：s = " 2-1 + 2 "
# 输出：3
#
#
# 示例 3：
#
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 3 * 10^5
# s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
# s 表示一个有效的表达式
# '+' 不能用作一元运算(例如， "+1" 和 "+(2 + 3)" 无效)
# '-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 是有效的)
# 输入中不存在两个连续的操作符
# 每个数字和运行的计算将适合于一个有符号的 32位 整数
#
#
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        s = "(" + s + ")"
        stack = []
        n = len(s)
        i = 0
        while i < n:
            c = s[i]
            # print(c)
            match c:
                case " ":
                    i += 1
                    continue
                case "+":
                    stack.append("+")
                    i += 1
                case "-":
                    stack.append("-")
                    i += 1
                case "(":
                    stack.append("(")
                    i += 1
                case ")":
                    lst = []
                    ans = 0
                    flag = ""
                    while stack:
                        x = stack.pop()
                        if x == "(":
                            for y in lst:
                                if y not in ("+", "-"):
                                    if flag == "+" or flag == "":
                                        ans += y
                                    elif flag == "-":
                                        ans -= y
                                else:
                                    flag = y

                            break
                        lst.insert(0, x)
                    stack.append(ans)
                    i += 1
                case _:
                    num = 0
                    for j in range(i, n):
                        if "0" <= s[j] <= "9":
                            num = num * 10 + int(s[j])
                            if j == n - 1:
                                i = n
                                break
                        else:
                            break
                    stack.append(num)
                    i = j
            # print(i)

        return stack[0]


# @lc code=end


#
# @lcpr case=start
# "1 + 1"\n
# @lcpr case=end

# @lcpr case=start
# " 2-1 + 2 "\n
# @lcpr case=end

# @lcpr case=start
# "(1+(4+5+2)-3)+(6+8)"\n
# @lcpr case=end

# @lcpr case=start
# "2147483647"\n
# @lcpr case=end

#

#
