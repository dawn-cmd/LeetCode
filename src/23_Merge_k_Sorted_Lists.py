from heapq import *
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
ListNode.__lt__ = lambda a, b: a.val < b.val  # type: ignore
class Solution:
    def mergeKLists(self, lists) -> Optional[ListNode]:
        ans = ListNode()
        cur = ans
        h = [head for head in lists if head]
        heapify(h)
        while h:
            tmp = heappop(h)
            if tmp.next:
                heappush(h, tmp.next)
            cur.next = tmp
            cur = cur.next
        return ans.next
