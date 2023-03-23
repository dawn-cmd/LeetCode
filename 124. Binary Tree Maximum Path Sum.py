# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    max_value = float("-inf")
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(now: Optional[TreeNode]) -> int:
            if now == None:
                return 0
            left_max = dfs(now.left)
            left_max = left_max if left_max > 0 else 0
            right_max = dfs(now.right)
            right_max = right_max if right_max > 0 else 0
            self.max_value = self.max_value if self.max_value > left_max + now.val + right_max else left_max + now.val + right_max
            return (left_max if left_max > right_max else right_max) + now.val

        ans = dfs(root)
        return max(ans, self.max_value)
