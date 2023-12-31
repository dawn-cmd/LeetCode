# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(left: TreeNode, right: TreeNode) -> bool:
            if left == right == None:
                return True
            if (left == None and right != None) or (right == None and left != None) or left.val != right.val:
                return False 
            return dfs(left.right, right.left) and dfs(left.left, right.right)
        
        return dfs(root.left, root.right)
