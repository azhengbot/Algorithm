#
# @lc app=leetcode.cn id=307 lang=python3
#
# [307] 区域和检索 - 数组可修改
#
# https://leetcode-cn.com/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (52.62%)
# Likes:    442
# Dislikes: 0
# Total Accepted:    41.2K
# Total Submissions: 82.4K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# 给你一个数组 nums ，请你完成两类查询。
#
#
# 其中一类查询要求 更新 数组 nums 下标对应的值
# 另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right
#
#
# 实现 NumArray 类：
#
#
# NumArray(int[] nums) 用整数数组 nums 初始化对象
# void update(int index, int val) 将 nums[index] 的值 更新 为 val
# int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含
# ）的nums元素的 和 （即，nums[left] + nums[left + 1], ..., nums[right]）
#
#
#
#
# 示例 1：
#
#
# 输入：
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# 输出：
# [null, 9, null, 8]
#
# 解释：
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1,2,5]
# numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
# 0 <= index < nums.length
# -100 <= val <= 100
# 0 <= left <= right < nums.length
# 调用 update 和 sumRange 方法次数不大于 3 * 10^4
#
#
#

# @lc code=start
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.st = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.st.update(1, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.st.query(1, left, right)


class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.tree = [{} for _ in range(4 * self.n)]
        self._build(p=1, l=0, r=self.n - 1)

    def _build(self, p: int, l: int, r: int):
        if l == r:
            # print(self.tree[p])
            self.tree[p]["l"], self.tree[p]["r"], self.tree[p]["data"] = (
                l,
                r,
                self.nums[l],
            )
            return

        mid = (l + r) // 2

        self._build(2 * p, l, mid)
        self._build(2 * p + 1, mid + 1, r)

        # print(p, self.tree, "+++++")
        self.tree[p]["l"], self.tree[p]["r"], self.tree[p]["data"] = (
            l,
            r,
            self.tree[2 * p]["data"] + self.tree[2 * p + 1]["data"],
        )

    def update(self, p: int, idx: int, val: int):
        l, r = self.tree[p]["l"], self.tree[p]["r"]
        if l == r:
            self.tree[p]["data"] = val
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(2 * p, idx, val)
        else:
            self.update(2 * p + 1, idx, val)

        self.tree[p]["data"] = self.tree[2 * p]["data"] + self.tree[2 * p + 1]["data"]

    def query(self, p: int, left: int, right: int):
        # print(p, self.tree, "======")
        l, r = self.tree[p]["l"], self.tree[p]["r"]
        if left <= l and r <= right:
            return self.tree[p]["data"]
        mid = (l + r) // 2
        ans = 0
        if left <= mid:
            ans += self.query(p * 2, left, right)
        if right > mid:
            ans += self.query(p * 2 + 1, left, right)

        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end
