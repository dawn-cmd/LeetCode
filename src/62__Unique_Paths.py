import numpy

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = numpy.zeros((n, m), dtype=int)
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i > 0: dp[i][j] += dp[i - 1][j]
                if j > 0: dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]

print(Solution().uniquePaths(m = 3, n = 7))
