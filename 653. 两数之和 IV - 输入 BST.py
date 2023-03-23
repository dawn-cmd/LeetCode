from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    h = set()
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool: 
        if root == None:
            return False
        if k - root.val in self.h:
            return True
        self.h.add(root.val)
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)
