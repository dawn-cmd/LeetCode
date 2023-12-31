from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        h = {
            '2': ['a', 'b', 'c'], 
            '3': ['d', 'e', 'f'], 
            '4': ['g', 'h', 'i'], 
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']}
        ans = []
        
        def dfs(digits: str, now: str):
            if digits == '':
                ans.append(now)
                return
            for c in h[digits[0]]:
                dfs(digits[1:], now + c)
         
        dfs(digits, '')
        return ans

print(Solution().letterCombinations(digits = "23"))
