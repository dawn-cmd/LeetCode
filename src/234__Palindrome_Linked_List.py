# Definition for singly-linked list.
class ListNode:

    __slots__ = 'val', 'next'

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next 

        def reverse_list(head: ListNode) -> ListNode:
            pre = None
            curr = head
            while curr:
                nextNode = curr.next
                curr.next = pre
                pre = curr
                curr = nextNode
            return pre

        slow = reverse_list(slow)
        first = head
        second = slow
        while first and second:
            if first.val != second.val:
                return False
            first, second = first.next, second.next
        return True

