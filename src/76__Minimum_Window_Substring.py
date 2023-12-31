class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        for c in t:  
            d[c] = d.get(c, 0) + 1
        # print(d)
        cnt = len(t)
        left = 0
        ans = ""
        for right in range(len(s)):
            if s[right] in d:
                if d[s[right]] > 0:
                    cnt -= 1
                d[s[right]] -= 1
            if cnt:
                continue
            while left < right and d.get(s[left], -1) != 0:
                if s[left] in d: 
                    d[s[left]] += 1
                left += 1
            # print(left, right)
            if ans == "" or right - left + 1 < len(ans): 
                ans = s[left: right + 1]
            d[s[left]] += 1
            left += 1
            cnt += 1
        return ans

print(Solution().minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))
