# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            print("Node is None")
            return []
        ans = [[root]]
        i = 0
        while i < len(ans):
            if len(ans[i]) == 0:
                break
            ans.append([])
            for node in ans[i]:
                if node.left:
                    ans[-1].append(node.left)
                if node.right:
                    ans[-1].append(node.right)
            i += 1
        ans = [[node.val for node in i] for i in ans]
        return ans[:-1]
