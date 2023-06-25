#
# @lc app=leetcode.cn id=1401 lang=python3
#
# [1401] 圆和矩形是否有重叠
#
# https://leetcode.cn/problems/circle-and-rectangle-overlapping/description/
#
# algorithms
# Medium (43.54%)
# Likes:    79
# Dislikes: 0
# Total Accepted:    12.6K
# Total Submissions: 25.3K
# Testcase Example:  '1\n0\n0\n1\n-1\n3\n1'
#
# 给你一个以 (radius, xCenter, yCenter) 表示的圆和一个与坐标轴平行的矩形 (x1, y1, x2, y2) ，其中 (x1,
# y1) 是矩形左下角的坐标，而 (x2, y2) 是右上角的坐标。
#
# 如果圆和矩形有重叠的部分，请你返回 true ，否则返回 false 。
#
# 换句话说，请你检测是否 存在 点 (xi, yi) ，它既在圆上也在矩形上（两者都包括点落在边界上的情况）。
#
#
#
# 示例 1 ：
#
#
# 输入：radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
# 输出：true
# 解释：圆和矩形存在公共点 (1,0) 。
#
#
# 示例 2 ：
#
#
# 输入：radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
# 输出：false
#
#
# 示例 3 ：
#
#
# 输入：radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
# 输出：true
#
#
#
#
# 提示：
#
#
# 1 <= radius <= 2000
# -10^4 <= xCenter, yCenter <= 10^4
# -10^4 <= x1 < x2 <= 10^4
# -10^4 <= y1 < y2 <= 10^4
#
#
#


# @lc code=start
class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        def get_min(x1, x2, x_center):
            if x1 <= x_center <= x2:
                return 0
            elif x1 > x_center:
                return x1 - x_center

            return x_center - x2

        x = get_min(x1, x2, xCenter)
        y = get_min(y1, y2, yCenter)

        return x**2 + y**2 <= radius**2


radius, xCenter, yCenter, x1, y1, x2, y2 = (1, 1, 1, 1, -3, 2, -1)
radius, xCenter, yCenter, x1, y1, x2, y2 = (1, 0, 0, 1, -1, 3, 1)
s = Solution()
res = s.checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2)
print(res)
# @lc code=end
