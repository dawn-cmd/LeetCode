from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        st, ed = 0, len(s)
        perm = []
        for i in range(len(s)):
            if s[i] == 'I':
                perm.append(st)
                st += 1
            else:
                perm.append(ed)
                ed -= 1
        perm.append(ed)
        return perm
