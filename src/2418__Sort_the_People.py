from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = [(heights[_], names[_]) for _ in range(len(names))]
        people = sorted(people, reverse=True)
        return [people[_][1] for _ in range(len(people))]

print(Solution().sortPeople(["Mary","John","Emma"], [180,165,170]))
