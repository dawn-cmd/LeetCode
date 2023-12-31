from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for i in range(k):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
        ans.append(nums[q[0]])
        for i in range(k, len(nums)):
            while q and q[0] < i - k + 1:
                q.popleft()
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            ans.append(nums[q[0]])
        return ans

print(Solution().maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
