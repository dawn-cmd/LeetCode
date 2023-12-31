from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        l = (sum(piles) - 1) // h + 1
        r = min(max(piles), (sum(piles) - len(piles) - 1)//(h - len(piles)) + 1)
        while l < r:
            mid = (l + r) >> 1
            cnt = sum((pile + mid - 1) // mid for pile in piles)
            if cnt <= h:
                r = mid
            else:
                l = mid + 1
        return l
