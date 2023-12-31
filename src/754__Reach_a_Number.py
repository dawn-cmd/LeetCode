from collections import defaultdict, deque
from turtle import st


class Solution:
    def reachNumber(self, target: int) -> int:
        q = deque()
        q.append((0, 0))
        while len(q):
            now, step = q.popleft()
            # print(now, step)
            if now + step + 1 == target:
                return step + 1
            q.append((now + step + 1, step + 1))
            if now - step - 1 == target:
                return step + 1
            q.append((now - step - 1, step + 1))
        return -1
    
print(Solution().reachNumber(2))
