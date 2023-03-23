from collections import deque


class Solution:

    def reverseParentheses(self, s: str) -> str:
        stk = deque()
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(i)
            elif s[i] == ')':
                st = stk.pop()
                ed = i
                s = s[:st + 1] + ''.join(reversed(s[st + 1:ed])) + s[ed:]
        return ''.join([x for x in s if x != '(' and x != ')'])

def main():
    print(Solution().reverseParentheses(s = "(ed(et(oc))el)"))

if __name__ == "__main__":
    main()