# Definition for singly-linked list.
from collections import defaultdict


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode):
        h = []
        id = head
        while id != None:
            if id in h:
                return id
            h.append(id)
            id = id.next 
        return None
