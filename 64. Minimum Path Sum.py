from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[float("inf")] * len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i > 0 and dp[i - 1][j] + grid[i][j] < dp[i][j]: dp[i][j] = dp[i - 1][j] + grid[i][j]
                if j > 0 and dp[i][j - 1] + grid[i][j] < dp[i][j]: dp[i][j] = dp[i][j - 1] + grid[i][j]
        return dp[-1][-1]

print(Solution().minPathSum(grid = [[1,2,3],[4,5,6]]))
