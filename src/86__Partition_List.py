# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=1, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        previous = ListNode()
        last = ListNode()
        p_now = previous
        l_now = last
        while head != None:
            if head.val < x:
                p_now.next = head
                head = head.next
                p_now = p_now.next
                p_now.next = None
            else:
                l_now.next = head
                head = head.next
                l_now = l_now.next
                l_now.next = None
        p_now.next = last.next
        return previous.next
