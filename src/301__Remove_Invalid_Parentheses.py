from collections import deque
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        q = deque()
        cnt_l = cnt_r = 0
        for i in range(len(s)):
            if s[i] == '(':
                cnt_l += 1
            elif s[i] == ')':
                cnt_r += 1 
        q.append((s, 0, cnt_l, cnt_r))

        def check(s: str) -> bool:
            # print(s, end=' ')
            cnt = 0
            for c in s:
                if c != '(' and c != ')':
                    continue
                cnt += 1 if c == '(' else -1
                if cnt < 0:
                    # print('False')
                    return False
            # print('True')
            return cnt == 0
        
        min_time = float('inf')
        ans = []
        h = set()
        while q:
            now, times, left, right = q.popleft()
            if now in h:
                continue
            else:
                h.add(now)
            # print(now, times, left, right)
            if check(now):
                if times > min_time:
                    break
                else:
                    min_time = times
                    ans.append(now)
                    continue
            for i in range(len(now)):
                if now[i] != '(' and now[i] != ')':
                    continue
                if now[i] == '(' and left < right:
                    continue
                if now[i] == ')' and left > right:
                    continue
                q.append((now[:i] + now[i + 1:], times + 1, (left - 1 if now[i] == '(' else left), (right - 1 if now[i] == ')' else right)))
        ans = set(ans)
        ans = list(ans)
        return ans

print(Solution().removeInvalidParentheses(s = "((()((s((((()"))
