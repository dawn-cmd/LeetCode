from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans

print(Solution().singleNumber(nums = [4,1,2,1,2]))
