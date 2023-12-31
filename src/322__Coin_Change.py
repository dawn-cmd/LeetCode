from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(amount + 1):
                if i + coin > amount:
                    continue
                dp[i + coin] = dp[i + coin] if dp[i + coin] < dp[i] + 1 else dp[i] + 1
        return -1 if dp[amount] == float('inf') else dp[amount]

print(Solution().coinChange(coins = [2], amount = 3))
