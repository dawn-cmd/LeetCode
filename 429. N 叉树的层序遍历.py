# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        ans = []

        def dfs(root: Node, ans: List[List[int]], h: int):
            if root == None:
                return
            if h == len(ans):
                ans.append([])
            ans[h].append(root.val)
            for child in root.children:
                dfs(child, ans, h + 1)
        
        dfs(root, ans, 0)
        return ans

def main():
    print(Solution().levelOrder())
