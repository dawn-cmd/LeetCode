# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        fa = {}

        def dfs(now: TreeNode, pre: TreeNode, fa: dict):
            if now is None:
                return
            fa[now] = pre
            dfs(now.left, now, fa)
            dfs(now.right, now, fa)
        
        dfs(root, None, fa)
        h = set()
        while p is not None:
            h.add(p)
            p = fa[p]
        while q is not None:
            if q in h:
                return q
            q = fa[q]
        return None
