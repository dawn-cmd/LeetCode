from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:

        def check_substring(a: str, b: str) -> bool:
            id = 0
            for c in b:
                while id < len(a) and a[id] != c:
                    id += 1
                if id == len(a): return False
                id += 1
            return True

        ans = -1
        for i, s1 in enumerate(strs):
            is_unique = True
            for j, s2 in enumerate(strs):
                if i == j: continue
                if check_substring(s2, s1):
                    is_unique = False
                    break
            if is_unique:
                ans = max(ans, len(s1))
        
        return ans

print(Solution().findLUSlength(["aba","cdc","eae"]))
