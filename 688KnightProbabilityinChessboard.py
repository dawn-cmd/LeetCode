class Solution:
    
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[float(0)] * n for _ in range(n)] for _ in range(k + 1)]
        for i in range(n):
            for j in range(n):
                dp[0][i][j] = float(1)
        for stage in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for di, dj in ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, -2), (-1, 2)):
                        if 0 <= i + di < n and 0 <= j + dj < n:
                            dp[stage][i][j] += dp[stage - 1][i + di][j + dj] / 8
        return dp[k][row][column]

def main():
    print(Solution().knightProbability(n = 3, k = 2, row = 0, column = 0))

if __name__ == "__main__":
    main()
