from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = []

        def dfs(root: TreeNode, ans: List[int]):
            if root == None:
                return
            dfs(root.left, ans)
            ans.append(root.val)
            dfs(root.right, ans)
        
        dfs(root1, ans)
        dfs(root2, ans)
        ans.sort()
        return ans
