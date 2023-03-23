# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None or root.left == None:
            return 
        if root.right == None:
            root.right = root.left
            root.left = None
            return 
        left, right = root.left, root.right
        self.flatten(left)
        self.flatten(right)
        root.right = left
        root.left = None
        while left.right != None:
            left = left.right
        left.right = right


