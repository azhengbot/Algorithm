from typing import List

# TODO 单调性，不是太好理解
class Solution:
    def trap(self, height: List[int]) -> int:

        # java用的是递减序列
        ans = 0
        s = []
        for h in height:
            accumulateWidth = 0

            while len(s) != 0 and s[-1][0] <= h:
                bottom = s[-1][0]
                accumulateWidth += s[-1][1]

                s.pop()

                if len(s) == 0:
                    continue

                up = min(h, s[-1][0])

                ans += accumulateWidth * (up - bottom)

            s.append([h, accumulateWidth + 1])

        return ans

        # 竖着找，找找两边最大值
        # n = len(height)
        # ans = 0

        # pre_max = [0 for i in range(n)]

        # after_max = [0 for i in range(n)]

        # pre_max[0] = height[0]
        # for i in range(1, n):
        #     pre_max[i] = max(height[i], pre_max[i - 1])

        # after_max[n - 1] = height[n - 1]
        # for i in range(n - 2, -1, -1):
        #     after_max[i] = max(height[i], after_max[i + 1])

        # # print(pre_max)
        # # print(after_max)

        # for i in range(1, n - 1):
        #     ans += min(pre_max[i], after_max[i]) - height[i]

        # return ans

        # 直接找会超时
        # n = len(height)
        # ans = 0
        # for i in range(1, n):

        #     pre = i - 1
        #     after = i + 1

        #     while pre >= 0:
        #         if height[i] == height[pre]:
        #             break
        #         if height[pre] > height[i]:
        #             break
        #         else:
        #             pre -= 1

        #     while after < n:
        #         if height[after] > height[i]:
        #             break
        #         else:
        #             after += 1

        #     if (
        #         pre >= 0
        #         and after < n
        #         and height[pre] > height[i]
        #         and height[after] > height[i]
        #     ):
        #         ans += (min(height[pre], height[after]) - height[i]) * (after - pre - 1)

        # return ans


s = Solution()
height = [0, 1, 2, 0, 3, 0, 1, 2, 0, 0, 4, 2, 1, 2, 5, 0, 1, 2, 0, 2]
height = [4, 2, 0, 3, 2, 5]
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
res = s.trap(height=height)
print(res)
