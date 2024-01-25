#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode.cn/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (37.56%)
# Likes:    2436
# Dislikes: 0
# Total Accepted:    419.2K
# Total Submissions: 1.1M
# Testcase Example:  '"(()"'
#
# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
# 
# 
# 示例 2：
# 
# 
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
# 
# 
# 示例 3：
# 
# 
# 输入：s = ""
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# s[i] 为 '(' 或 ')'
# 
# 
# 
# 
#

# @lc code=start
from functools import lru_cache


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        ans = 0
        stack = [-1]
        if not s:
            return 0
        for i in range(n):
            # print(i, stack)
            if s[i] == "(":
                if stack[-1] == -1:
                    ans = max(ans, i)  
                else:
                    ans = max(ans, i - stack[-1] -1)             
                stack.append(i)
                
            elif stack[-1] != -1 and s[stack[-1]] == "(":
                stack.pop()
            else:
                ans = max(ans, i - stack[-1] - 1)
                stack.append(i)

        # print(stack) 
        if i == n-1:
            ans = max(i - stack[-1], ans)
        
        return ans if ans != 1 else 0
                        

                    
                
            
        
                    

        
# dic = "((((()())()()))()(()))"
            
# @lc code=end

