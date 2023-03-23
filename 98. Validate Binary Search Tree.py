# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        parameter = {"ans": True, "pre": None}

        def dfs(now: Optional[TreeNode], parameter: dict):
            if now == None or parameter["ans"] == False:
                return
            dfs(now.left, parameter)
            if parameter["pre"] != None and parameter["pre"] >= now.val:
                parameter["ans"] = False
                return
            parameter["pre"] = now.val
            dfs(now.right, parameter)

        dfs(root, parameter)
        return parameter["ans"]
