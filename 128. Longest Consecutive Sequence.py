from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        h = defaultdict(int)

        def dfs(now: int) -> int:
            if h[now] != 0:
                return h[now]
            if (now - 1) in nums:
                h[now] = dfs(now - 1) + 1
                return h[now]
            else:
                return 1

        ans = 0
        for num in nums:
            ans = max(ans, dfs(num))
        return ans

print(Solution().longestConsecutive([100,4,200,1,3,2]))
        