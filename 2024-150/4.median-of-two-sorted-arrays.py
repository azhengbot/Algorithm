#
# @lc app=leetcode.cn id=4 lang=python3
# @lcpr version=30204
#
# [4] 寻找两个正序数组的中位数
#
# https://leetcode.cn/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (42.66%)
# Likes:    7260
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 2.8M
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
#
# 算法的时间复杂度应该为 O(log (m+n)) 。
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#
#
# 示例 2：
#
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#
#
#
#
#
#
# 提示：
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        z = m + n
        mid = (z - 1) // 2
        i = 0
        j = 0
        k = 0

        ans = []

        while i < m or j < n:
            if i < m and j < n:
                if nums1[i] <= nums2[j]:
                    ans.append(nums1[i])
                    i += 1
                else:
                    ans.append(nums2[j])
                    j += 1
            elif i < m:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
            # print(ans)
            if k == mid:
                if z % 2:
                    return ans[-1]
            if k == mid + 1:
                print(ans)
                return (ans[-1] + ans[-2]) / 2
            k += 1


# @lc code=end


#
# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#
