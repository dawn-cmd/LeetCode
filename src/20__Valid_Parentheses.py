from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stk = deque()
        h = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in ['(', '[', '{']:
                stk.append(c)
                continue
            if len(stk) == 0 or h[c] != stk[-1]:
                return False
            stk.pop()
        return len(stk) == 0

def main():
    print(Solution().isValid(s = "()[]{}"))

if __name__ == "__main__":
    main()
                    
