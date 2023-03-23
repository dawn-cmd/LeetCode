class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        f = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        f[0][0] = True

        def match(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        for i in range(len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if match(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if match(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[len(s)][len(p)]

        

print(Solution().isMatch(s = "aaa", p = "a"))
