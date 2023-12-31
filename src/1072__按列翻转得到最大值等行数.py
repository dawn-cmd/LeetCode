from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        h = {}
        ans = 0
        for line in matrix:
            trans = ""
            for i in range(1, len(line)):
                trans += "0" if line[i - 1] == line[i] else "1"
            h[trans] = h.get(trans, 0) + 1
            ans = max(ans, h[trans])
        return ans
