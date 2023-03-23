from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]
        ans = []
        
        def getAllSplit(s: str) -> List[str]:
            ans = []
            if len(s) == 1:
                return [s]
            if