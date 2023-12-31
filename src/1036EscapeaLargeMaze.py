from collections import deque
from typing import Deque, List


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if len(blocked) < 2:
            return True
        blocked = set([tuple(point) for point in blocked])
        source, target = [tuple(point) for point in [source, target]]

        def dfs(source: tuple, target: tuple, blocked: set) -> bool:
            h = set([source])
            q = deque([source])
            orients = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            size_limit = len(blocked) * (len(blocked) - 1) // 2 - 1
            while q:
                now = q.popleft()
                for orient in orients:
                    next = (now[0] + orient[0], now[1] + orient[1])
                    if next[0] < 0 or next[0] >= 1e6 or next[1] < 0 or next[1] >= 1e6 or next in blocked or next in h:
                        continue
                    if next == target:
                        return True
                    q.append(next)
                    h.add(next)
                    size_limit -= 1
                    if size_limit < 0:
                        return True
            return False

        return dfs(source, target, blocked) and dfs(target, source, blocked)

def main():
    solution = Solution()
    print(solution.isEscapePossible(blocked = [], source = [0,0], target = [999999,999999]))

if __name__ == "__main__":
    main()
