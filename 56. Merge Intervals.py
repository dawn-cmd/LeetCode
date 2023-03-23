from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 0
        while i < len(intervals):
            max_r, l, j = intervals[i][1], len(intervals), i
            while j < l and intervals[j][0] <= max_r:
                max_r = max_r if max_r > intervals[j][1] else intervals[j][1]
                j += 1
            intervals[i:j] = [[intervals[i][0], max_r]]
            i += 1
        return intervals

print(Solution().merge(intervals = [[1,4],[0,2],[3,5]]))
