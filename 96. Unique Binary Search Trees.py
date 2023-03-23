class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1]
        for i in range(1, n + 1):
            dp.append(0)
            for j in range(i):
                dp[-1] += dp[j] * dp[i - 1 - j]
        return dp[-1]

print(Solution().numTrees(4))
