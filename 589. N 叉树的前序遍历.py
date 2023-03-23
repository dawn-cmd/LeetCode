from typing import List


class Node:

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:

    def preorder(self, root: Node) -> List[int]:
        if root == None:
            return []
        ans = [root.val]
        for child in root.children:
            if child == None:
                continue
            ans += self.preorder(child)
        return ans