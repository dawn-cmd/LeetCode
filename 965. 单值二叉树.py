# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root.left == root.right == None:
            return True
        if root.left == None:
            return self.isUnivalTree(root.right) and root.val == root.right.val
        if root.right == None:
            return self.isUnivalTree(root.left) and root.val == root.left.val
        if not root.val == root.right.val == root.left.val:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
