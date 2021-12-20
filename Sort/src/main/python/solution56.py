from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        n = len(intervals)

        ans = []

        start_0, start_1 = intervals[0]

        i = 0
        while i < n:
            if intervals[i][0] < start_1:
                if intervals[i][1] > start_1:
                    start_1 = intervals[i][1]
                i += 1

            elif intervals[i][0] > start_1:
                ans.append([start_0, start_1])

                start_0, start_1 = intervals[i]

                i += 1

            elif intervals[i][0] == start_1:
                start_1 = intervals[i][1]
                i += 1

        ans.append([start_0, start_1])

        return ans
