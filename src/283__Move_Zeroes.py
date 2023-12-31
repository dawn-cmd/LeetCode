from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        id = 0
        for i in range(len(nums)):
            if nums[i] == 0: 
                continue
            nums[i], nums[id] = nums[id], nums[i]
            id += 1

nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums) 
