# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        id = head
        l = []
        while id:
            l.append(id)
            id = id.next
            l[-1].next = None
        l[left - 1 : right] = reversed(l[left - 1 : right])
        head = l[0]
        id = head
        for node in l[1:]:
            id.next = node
            id = id.next
        return head
