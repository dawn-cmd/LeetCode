class Solution:
    def reformatNumber(self, number: str) -> str:
        ans = number[:]
        ans = ans.replace(' ', '')
        ans = ans.replace('-', '')
        id = 0
        while len(ans) - id > 4:
            id += 3
            ans = ans[:id] + '-' + ans[id:]
            id += 1
        if len(ans) - id <= 3:
            return ans
        id += 2
        ans = ans[:id] + '-' + ans[id:]
        return ans

print(Solution().reformatNumber("123 4-567"))
