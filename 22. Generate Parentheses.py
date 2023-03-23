from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(now: str, left: int, right: int):
            if left == right == 0: return ans.append(now)
            if now.count(')') > now.count('('): return
            if left: dfs(''.join([now, '(']), left - 1, right)
            if right: dfs(''.join([now, ')']), left, right - 1)
        
        dfs('', n, n)
        return ans

print(Solution().generateParenthesis(8))

