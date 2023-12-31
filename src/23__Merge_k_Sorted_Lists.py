from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        st = []
        get_num = lambda node: [] if node == None else [node.val] + get_num(node.next)  # Turn a linked-list to a list
        for head in lists:
            st += get_num(head)  # Gather all the values in st[]
        if len(st) == 0: return None
        st.sort()
        ans = ListNode()
        now = ans

        #  Turn st[] back to a linked-list
        for num in st:
            now.next = ListNode(num)
            now = now.next

        return ans.next  # "ans" is just a virtual head, ans.next is answer
