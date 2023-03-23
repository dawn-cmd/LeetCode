from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r = 0
        for i in range(len(nums)):
            if i > r: return False
            if i + nums[i] > r: r = i + nums[i]
        return True
        
print(Solution().canJump([2,3,1,1,4]))
