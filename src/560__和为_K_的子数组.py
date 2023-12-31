from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = nums[0]
        j = 0
        ans = 0
        for i in range(len(nums)):
            while (j < i or (s < k and j < len(nums) - 1)):
                j += 1
                s += nums[j]
            if s == k:
                ans += 1
            s -= nums[i]
        return ans
