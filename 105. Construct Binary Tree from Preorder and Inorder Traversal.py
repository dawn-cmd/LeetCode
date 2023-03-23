# Definition for a binary tree node.
from typing import List, Optional



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        h = {inorder[i]: i for i in range(len(inorder))}

        def build(p_left: int, p_right: int, i_left: int, i_right: int) -> Optional[TreeNode]:
            if p_left > p_right or i_left > i_right:  # if it is an empty tree
                return None
            now = TreeNode(preorder[p_left])  # now represents the root of the tree
            id = h[preorder[p_left]]
            now.left = build(p_left + 1, p_left + (id - i_left), i_left, id - 1)
            now.right = build(p_left + (id - i_left) + 1, p_right, id + 1, i_right)
            return now
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
