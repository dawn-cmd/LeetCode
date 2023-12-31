from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def compare(a: int, b: int) -> int:
            return a if a > b else b

        now = [-prices[0], 0, 0]
        for i in range(1, len(prices)):
            now = [
                compare(now[0], now[2] - prices[i]), 
                now[0] + prices[i], 
                compare(now[2], now[1])
            ]
        return compare(now[1], now[2])

print(Solution().maxProfit(prices = [1,2,3,0,2]))
