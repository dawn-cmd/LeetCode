# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        base = None
        max_freq = 0
        freq = 0

        def update(val):
            nonlocal base, res, max_freq, freq
            if freq > max_freq:
                max_freq = freq
                res = [val]
            elif freq == max_freq:
                res.append(val)

        def dfs(cur: Optional[TreeNode]):
            nonlocal base, res, max_freq, freq
            if not cur:
                return
            dfs(cur.left)
            if base == None:
                base = cur.val
                freq = 1
                max_freq = 1
                res = [cur.val]
            elif cur.val == base:
                freq += 1
                update(cur.val)
            else:
                base = cur.val
                freq = 1
                update(cur.val)
            dfs(cur.right)

        dfs(root)
        return res
