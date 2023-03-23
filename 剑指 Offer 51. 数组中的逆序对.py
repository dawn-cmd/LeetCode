from bisect import bisect_left
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        q = []
        for num in nums[::-1]:
            pos = bisect_left(q, num)
            ans += pos
            q[pos:pos] = [num]
        return ans

print(Solution().reversePairs([7,5,6,4]))
