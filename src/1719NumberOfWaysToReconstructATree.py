from collections import Counter, defaultdict
from email.policy import default
from sys import maxsize
from typing import List

from sklearn import neighbors


class Solution:
    
    def checkWays(self, pairs: List[List[int]]) -> int:
        adj = defaultdict(set)
        for pair in pairs:
            adj[pair[0]].add(pair[1])
            adj[pair[1]].add(pair[0])
        root = next((node for node, neighbours in adj.items() if len(neighbours) == len(adj) - 1), -1)
        if root == -1:
            return 0
        
        ans = 1
        for node, neighbors in adj.items():
            if node == root:
                continue
            currDegree = len(neighbors)
            parent = -1
            parentDegree = maxsize
            for neighbour in neighbors:
                if currDegree <= len(adj[neighbour]) < parentDegree:
                    parent = neighbour
                    parentDegree = len(adj[neighbour])
            if parent == -1 or any(neighbour != parent and neighbour not in adj[parent] for neighbour in neighbors):
                return 0
            
            if parentDegree == currDegree:
                ans = 2

        return ans