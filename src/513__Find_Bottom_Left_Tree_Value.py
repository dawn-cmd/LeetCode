# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        stk = []

        def dfs(now: TreeNode, layer: int):
            if now == None:
                return
            if layer >= len(stk):
                stk.append([])
            dfs(now.left, layer + 1)
            stk[layer].append(now.val)
            dfs(now.right, layer + 1)
        
        dfs(root, 0)
        return stk[-1][0]
