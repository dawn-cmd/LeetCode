from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        pmax = 0
        for p in prices[::-1]:
            if p > pmax:
                pmax = p
                continue
            ans = ans if ans > pmax - p else pmax - p
        return ans

print(Solution().maxProfit([7,1,5,3,6,4]))
