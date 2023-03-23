from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        id_mx = height.index(max(height))

        def count_half(height: List[int]) -> int:
            ans, h_mx = 0, -1
            for h in height:
                if h > h_mx: h_mx = h
                else: ans += h_mx - h
            return ans

        return count_half(height[:id_mx]) + count_half(height[:id_mx:-1])

print(Solution().trap([2, 0, 2]))
