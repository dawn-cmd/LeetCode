class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        cnt = 0
        for c in s:
            cnt += 1 if c == '(' else -1
            if cnt == 1 and c == '(' or cnt == 0 and c == ')':
                continue
            ans += c
        return ans

def main():
    print(Solution().removeOuterParentheses(s = "(()())(())(()(()))"))

if __name__ == "__main__":
    main()
