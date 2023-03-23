# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def larger(a: int, b: int):
            return a if a > b else b

        if root is None:
            return 0

        h = {}

        def dfs(now: TreeNode, get: bool, h) -> int:
            if now is None:
                return 0
            if (now, get) in h:
                return h[(now, get)]
            if get == True:
                h[(now, get)] = dfs(now.left, False, h) + dfs(now.right, False, h) + now.val
                return h[(now, get)]
            else:
                h[(now, get)] = larger(dfs(now.left, True, h), dfs(now.left, False, h)) + larger(dfs(now.right, True, h), dfs(now.right, False, h))
                return h[(now, get)]
        
        return larger(dfs(root, True, h), dfs(root, False, h))
