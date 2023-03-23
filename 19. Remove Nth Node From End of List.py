# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None and n == 1:
            return None
        l = []
        i = head
        while i != None:
            l.append(i)
            i = i.next
        if n == len(l):
            return l[1]
        l[-n - 1].next = l[-n].next
        return head
