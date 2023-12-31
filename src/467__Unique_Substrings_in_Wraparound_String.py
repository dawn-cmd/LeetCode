from collections import defaultdict


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = defaultdict(int)
        cnt = 1
        for i in range(len(p)):
            if i > 0 and (ord(p[i]) - ord(p[i - 1])) % 26 == 1:
                cnt += 1
            else:
                cnt = 1
            dp[p[i]] = max(dp[p[i]], cnt)
        return sum(dp.values())

def main():
    print(Solution().findSubstringInWraproundString(p = "cac"))

if __name__ == "__main__":
    main()

