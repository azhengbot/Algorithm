#
# @lc app=leetcode.cn id=1654 lang=python3
#
# [1654] 到家的最少跳跃次数
#
# https://leetcode.cn/problems/minimum-jumps-to-reach-home/description/
#
# algorithms
# Medium (31.19%)
# Likes:    155
# Dislikes: 0
# Total Accepted:    15.9K
# Total Submissions: 45.3K
# Testcase Example:  '[14,4,18,1,15]\n3\n15\n9'
#
# 有一只跳蚤的家在数轴上的位置 x 处。请你帮助它从位置 0 出发，到达它的家。
#
# 跳蚤跳跃的规则如下：
#
#
# 它可以 往前 跳恰好 a 个位置（即往右跳）。
# 它可以 往后 跳恰好 b 个位置（即往左跳）。
# 它不能 连续 往后跳 2 次。
# 它不能跳到任何 forbidden 数组中的位置。
#
#
# 跳蚤可以往前跳 超过 它的家的位置，但是它 不能跳到负整数 的位置。
#
# 给你一个整数数组 forbidden ，其中 forbidden[i] 是跳蚤不能跳到的位置，同时给你整数 a， b 和 x
# ，请你返回跳蚤到家的最少跳跃次数。如果没有恰好到达 x 的可行方案，请你返回 -1 。
#
#
#
# 示例 1：
#
#
# 输入：forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
# 输出：3
# 解释：往前跳 3 次（0 -> 3 -> 6 -> 9），跳蚤就到家了。
#
#
# 示例 2：
#
#
# 输入：forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
# 输出：-1
#
#
# 示例 3：
#
#
# 输入：forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
# 输出：2
# 解释：往前跳一次（0 -> 16），然后往回跳一次（16 -> 7），跳蚤就到家了。
#
#
#
#
# 提示：
#
#
# 1
# 1
# 0
# forbidden 中所有位置互不相同。
# 位置 x 不在 forbidden 中。
#
#
#

from collections import deque

# @lc code=start
from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        dq = deque([])
        dq.append((0, 1, 0))

        m = max(max(forbidden) + a, x) + b
        used = [[False, False] for _ in range(m + 1)]
        sf = set(forbidden)

        while len(dq):
            first, action, cnt = dq.popleft()
            if first == x:
                return cnt

            ni = first + a
            if ni >= 0 and ni <= m and (ni not in sf) and (not used[ni][0]):
                # continue
                used[ni][0] = True
                dq.append((ni, 1, cnt + 1))

            if action == 1:
                nj = first - b
                if nj >= 0 and nj <= m and (nj not in sf) and (not used[nj][1]):
                    used[nj][1] = True
                    dq.append((nj, -1, cnt + 1))

        return -1


# @lc code=end

forbidden = [1, 6, 2, 14, 5, 17, 4]
a = 16
b = 9
x = 7

s = Solution()
res = s.minimumJumps(forbidden, a, b, x)
print(res)
