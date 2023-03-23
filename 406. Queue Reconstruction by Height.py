from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = []
        for p in people:
            if len(ans) <= p[1]:
                ans.append(p)
            else:
                ans.insert(p[1], p)
        return ans

print(Solution().reconstructQueue(people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]))
