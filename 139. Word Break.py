from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False for _ in range(len(s))]
        for i in range(len(s)):
            for word in wordDict:
                if i + 1 < len(word):
                    continue
                # print(s[i - len(word) + 1: i + 1], s[i - len(word) + 1: i + 1] in wordDict)
                if not (s[i - len(word) + 1: i + 1] in wordDict):
                    continue
                if i + 1 == len(word):
                    dp[i] = True
                    break
                dp[i] = dp[i - len(word)]
                if dp[i]:
                    break
        # print(dp)
        return dp[-1]

print(Solution().wordBreak("dogs", ["dog","s","gs"]))
