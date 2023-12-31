# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur is not None and cur.next is not None:
            cur.val += cur.next.val
            cur.next.val = cur.val - cur.next.val
            cur.val = cur.val - cur.next.val
            cur = cur.next.next
        return head
