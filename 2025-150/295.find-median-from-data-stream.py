#
# @lc app=leetcode.cn id=295 lang=python3
# @lcpr version=30204
#
# [295] 数据流的中位数
#
# https://leetcode.cn/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (56.21%)
# Likes:    1097
# Dislikes: 0
# Total Accepted:    198.7K
# Total Submissions: 353K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
  '[[],[1],[2],[],[3],[]]'
#
# 中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。
# 
# 
# 例如 arr = [2,3,4] 的中位数是 3 。
# 例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
# 
# 
# 实现 MedianFinder 类:
# 
# 
# 
# MedianFinder() 初始化 MedianFinder 对象。
# 
# 
# void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
# 
# 
# double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10^-5 以内的答案将被接受。
# 
# 
# 
# 示例 1：
# 
# 输入
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# 输出
# [null, null, null, 1.5, null, 2.0]
# 
# 解释
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
# 
# 提示:
# 
# 
# -10^5 <= num <= 10^5
# 在调用 findMedian 之前，数据结构中至少有一个元素
# 最多 5 * 10^4 次调用 addNum 和 findMedian
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.max_heap = [] 
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            heappush(self.max_heap, -num)             
            a = heappop(self.max_heap)
            heappush(self.min_heap, -a)
        else:
            heappush(self.min_heap, num)
            b = heappop(self.min_heap)
            heappush(self.max_heap, -b)


    def findMedian(self) -> float:
        # print("+++", self.max_heap)
        # print(self.min_heap)
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end



