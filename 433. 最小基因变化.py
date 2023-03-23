from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        h = set([start])
        q = deque([(start, 0)])
        while q:
            now, step = q.popleft()
            if now == end:
                return step
            for i in range(len(now)):
                for j in ['A', 'C', 'G', 'T']:
                    tmp = list(now)
                    tmp[i] = j
                    tmp = ''.join(tmp)
                    if tmp in bank and tmp not in h:
                        q.append((tmp, step + 1))
                        h.add(tmp)
        return -1

def main():
    print(Solution().minMutation(start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]))

if __name__ == "__main__":
    main()
            