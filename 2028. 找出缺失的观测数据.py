from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        tot = mean * (n + len(rolls)) - sum(rolls)
        if tot > n * 6 or tot < n:
            return []
        ans = [0 for _ in range(n)]
        for i in range(n):
            ans[i] = min(6, tot - (n - i - 1))
            tot -= ans[i]
        return ans

def main():
    print(Solution().missingRolls(rolls = [1,5,6], mean = 3, n = 4))

if __name__ == "__main__":
    main()
