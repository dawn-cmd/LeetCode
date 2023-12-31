from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [nums[0], max(nums[1], nums[0])]
        for i in range(2, len(nums)):
            dp[-1], dp[-2] = max(dp[-2] + nums[i], dp[-1]), dp[-1]
        return dp[-1]

print(Solution().rob([2,7,9,3,1]))
