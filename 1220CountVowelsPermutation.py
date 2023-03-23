class Solution:
    MOD = int(1e9 + 7)
    def countVowelPermutation(self, n: int) -> int:
        if n == 1:
            return 5
        dp = [[1, 0] for i in range(5)]
        next = [[1], [0, 2], [0, 1, 3, 4], [2, 4], [0]]
        now = 0
        for i in range(1, n):
            now ^= 1
            for j in range(5):
                dp[j][now] = sum([dp[k][now ^ 1] for k in next[j]]) % self.MOD
        return sum([dp[i][now] for i in range(5)]) % self.MOD
    
def main():
    solution = Solution()
    print(solution.countVowelPermutation(5))

if __name__ == "__main__":
    main()
            
