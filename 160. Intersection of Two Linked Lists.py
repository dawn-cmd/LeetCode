# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        la, lb = [], []

        def setup(head: ListNode, l: List):
            while head != None:
                l.append(head)
                head = head.next
            return l
        
        la = setup(headA, la)
        lb = setup(headB, lb)
        ans = None
        ia, ib = len(la) - 1, len(lb) - 1
        while ia >= 0 and ib >= 0:
            if la[ia] == lb[ib]:
                ans = la[ia]
                ia, ib = ia - 1, ib - 1
            else:
                break
        return ans
