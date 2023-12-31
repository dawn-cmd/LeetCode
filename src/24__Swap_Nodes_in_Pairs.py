# Definition for singly-linked list.
from typing import Optional


class ListNode:
    """
    val: the value of the node
    next: the point to next node
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Solution to this problem
    """
    
    @staticmethod
    def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swap pairs
        """
        if head is None or head.next is None:
            return head
        now = head
        head = head.next
        pre = None
        while now is not None and now.next is not None:
            tmp = now.next
            now.next = tmp.next
            tmp.next = now
            if pre is not None:
                pre.next = tmp
            pre = now
            now = now.next
        return head
