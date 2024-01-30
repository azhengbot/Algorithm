#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
# https://leetcode.cn/problems/min-stack/description/
#
# algorithms
# Medium (59.34%)
# Likes:    1714
# Dislikes: 0
# Total Accepted:    539.5K
# Total Submissions: 908.3K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
# 
# 实现 MinStack 类:
# 
# 
# MinStack() 初始化堆栈对象。
# void push(int val) 将元素val推入堆栈。
# void pop() 删除堆栈顶部的元素。
# int top() 获取堆栈顶部的元素。
# int getMin() 获取堆栈中的最小元素。
# 
# 
# 
# 
# 示例 1:
# 
# 
# 输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# 输出：
# [null,null,null,null,-3,null,0,-2]
# 
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
# 
# 
# 
# 
# 提示：
# 
# 
# -2^31 <= val <= 2^31 - 1
# pop、top 和 getMin 操作总是在 非空栈 上调用
# push, pop, top, and getMin最多被调用 3 * 10^4 次
# 
# 
#

from collections import Counter

# @lc code=start
from heapq import heappop, heappush


class MinStack:

    def __init__(self):
        self.min = float("inf")
        self.stack = []
        self.heap = []
        self.cnt = Counter()

    def push(self, val: int) -> None:
        self.stack.append(val)
        heappush(self.heap, val)
        self.cnt[val] += 1

    def pop(self) -> None:
        val = self.stack.pop()
        # print(self.stack, "++++++++")
        self.cnt[val] -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        val = heappop(self.heap)
        # print(self.heap, self.cnt, val)
        while self.cnt[val] <= 0:
            val = heappop(self.heap)
        
        heappush(self.heap, val)
        return val
        



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

