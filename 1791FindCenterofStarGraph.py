from collections import defaultdict
from typing import List


class Solution:
    
    def findCenter(self, edges: List[List[int]]) -> int:
        adj = defaultdict(set)
        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
        for node, nxt in adj.items():
            if len(nxt) == len(adj) - 1:
                return node
    
def main():
    print(Solution().findCenter(edges = [[1,2],[5,1],[1,3],[1,4]]))

if __name__ == "__main__":
    main()