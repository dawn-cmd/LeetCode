# Definition for singly-linked list.
from audioop import reverse


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def get_num(l: ListNode) -> str:
            return str(l.val) if not l.next else  get_num(l.next) + str(l.val)
        
        ans = str(int(get_num(l1)) + int(get_num(l2)))
        ans = "".join(list(reversed(ans))) 
        
        def build(l: ListNode, num: str) -> ListNode:
            if len(num) == 1:
                l.val = int(num)
                return l
            l.val = int(num[0])
            l.next = build(ListNode(), num[1:])
            return l

        l3 = build(ListNode(), ans)
        
        return l3

