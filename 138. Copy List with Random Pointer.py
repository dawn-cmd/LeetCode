# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        h = {}
        def check(node: Node) -> Node:
            if node == None: return None
            if node in h: return h[node]
            ans = Node(node.val)
            h[node] = ans
            ans.next = check(node.next)
            ans.random = check(node.random)
            return ans
        return check(head)
