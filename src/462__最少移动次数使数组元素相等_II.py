from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        target = nums[len(nums) // 2]
        ans = sum([abs(num - target) for num in nums])
        return ans
