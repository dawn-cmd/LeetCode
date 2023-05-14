class Solution:
    def toInt(self, s):
        ans = 0
        for c in s:
            ans = ans * 2 + int(c)
        return ans

    def help(self, s, l, st, ed):
        h = set()
        for i in range(len(s) - l + 1):
            if st <= self.toInt(s[i:i + l]) <= ed:
                h.add(s[i:i + l])
        return len(h) == ed - st + 1

    def queryString(self, s: str, n: int) -> bool:
        if n == 1:
            return s.find('1') != -1
        l = 30
        while (1 << l) >= n:
            l -= 1
        return self.help(s, l, (1 << (l - 1)), (1 << l) - 1) and self.help(s, l + 1, (1 << l), n)


print(Solution().queryString(s="0110", n=4))
