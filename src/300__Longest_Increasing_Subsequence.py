from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                dp[i] = dp[i] if dp[i] >= dp[j] + 1 else dp[j] + 1
        return max(dp)

print(Solution().lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))
