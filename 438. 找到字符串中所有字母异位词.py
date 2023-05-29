from typing import List


class Solution:
    def initStr(self, s: str) -> str:
        l = list(s)
        l.sort()
        return "".join(l)

    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = self.initStr(p)
        ans = []
        for i in range(len(s) - len(p) + 1):
            if (self.initStr(s[i:i + len(p)]) == p):
                ans.append(i)
        return ans

if __name__ == "__main__":
    print(Solution().findAnagrams(s = "abab", p = "ab"))
