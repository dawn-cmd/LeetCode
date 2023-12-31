from collections import deque
import sys
from typing import List


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        g = [[] for _ in range(len(patience))]  
        for edge in edges:
            g[edge[0]].append(edge[1])
            g[edge[1]].append(edge[0])  # make graph
        length = [sys.maxsize for _ in range(len(g))]

        def bfs(length: List[int]):  # calculate the shortest way from 0 to n
            h = {0}
            q = deque([(0, 0)])
            while q:
                id, l = q.popleft()
                length[id] = min(length[id], l * 2)
                for next in g[id]:
                    if next in h:
                        continue
                    h.add(next)
                    q.append((next, l + 1))
        
        bfs(length)
        ans = -1
        for i in range(1, len(g)):
            if patience[i] >= length[i]:
                ans = max(ans, length[i] + 1)
            else:
                ans = max(ans, (length[i] - 1) // patience[i] * patience[i] + length[i] + 1)
        return ans
    
def main():
    print(Solution().networkBecomesIdle(edges = [[0,1],[0,2],[1,2]], patience = [0,10,10]))

if __name__ == "__main__":
    main()
