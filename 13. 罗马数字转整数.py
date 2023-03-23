class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = d[s[len(s) - 1]]
        for i in range(len(s) - 1):
            if d[s[i]] < d[s[i + 1]]:
                ans -= d[s[i]]
            else:
                ans += d[s[i]]
        return ans

def main():
    print(Solution().romanToInt(s = "LVIII"))

if __name__ == "__main__":
    main()
