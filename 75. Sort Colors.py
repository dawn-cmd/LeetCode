from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]: nums[j], nums[j + 1] = nums[j + 1], nums[j]

nums = [2,0,2,1,1,0]
Solution().sortColors(nums)
print(nums)
