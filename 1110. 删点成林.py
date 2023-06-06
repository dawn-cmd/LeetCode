# Definition for a binary tree node.
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = []

    def dfs(self, cur: TreeNode, to_delete: List[int]):
        if cur == None:
            return
        if cur.val in to_delete:
            if cur.left != None:
                self.ans.append(cur.left)
            if cur.right != None:
                self.ans.append(cur.right)
            if cur in self.ans:
                self.ans.remove(cur)
        self.dfs(cur.left, to_delete)
        self.dfs(cur.right, to_delete)
        if cur.left != None and cur.left.val in to_delete:
            cur.left = None
        if cur.right != None and cur.right.val in to_delete:
            cur.right = None

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.ans = []
        self.ans.append(root)
        self.dfs(root, to_delete)
        return self.ans
