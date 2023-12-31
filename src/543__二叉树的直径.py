# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ans = 1

    def dfs(self, cur: TreeNode, depth: int):
        deepest_leaf = depth
        left_depth = depth if cur.left == None else self.dfs(cur.left, depth + 1)
        right_depth = depth if cur.right == None else self.dfs(cur.right, depth + 1)
        deepest_leaf = max(left_depth, right_depth)
        self.ans = max(self.ans, left_depth - depth + right_depth - depth + 1)
        return deepest_leaf


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        self.ans = 1
        self.dfs(root, 1)
        return self.ans - 1
