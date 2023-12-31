from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i, num in enumerate(nums[1:]):
            dp.append(max(dp[-1] + num, num))
        return max(dp)

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
