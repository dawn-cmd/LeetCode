# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    is_find = True

    def dfs(self, root) -> int:
        if root == None:
            return 0
        lh = self.dfs(root.left)
        rh = self.dfs(root.right)
        if abs(lh - rh) > 1:
            self.is_find = False
        return (lh if lh > rh else rh) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root)
        return self.is_find
