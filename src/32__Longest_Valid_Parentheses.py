from collections import deque


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        h = [0] * len(s)  # 0 is valid, 1 is invalid
        st = deque()  # stack for parentheses pair

        for i, c in enumerate(s):
            if c == '(': st.append((c, i))
            elif len(st) and st[-1][0] == '(': st.pop()
            else: st.append((c, i))

        for item in st: h[item[1]] = 1
        ans = cnt = 0  # cnt is the longest consessive 0

        for num in h:
            if num == 0: cnt += 1
            else: ans, cnt = max(ans, cnt), 0
        if cnt: ans = max(ans, cnt)
        return ans

print(Solution().longestValidParentheses(")()())"))
