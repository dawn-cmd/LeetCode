# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        fast = head
        slow = head
        breakp = None
        while fast != None and fast.next != None:
            breakp = slow
            slow = slow.next
            fast = fast.next.next
        right = self.sortList(breakp.next)
        breakp.next = None
        left = self.sortList(head)

        def merge(left: ListNode, right: ListNode) -> ListNode:
            ans = ListNode()
            now = ans
            while left != None and right != None:
                if left.val <= right.val:
                    now.next = left
                    now = now.next
                    left = left.next
                else:
                    now.next = right
                    now = now.next
                    right = right.next
            if left != None:
                now.next = left
            else:
                now.next = right
            return ans.next
        
        return merge(left, right)
