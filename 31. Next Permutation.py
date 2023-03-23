from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        key = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                key = i - 1
                break
        # print(key)
        if key == -1:
            nums[:] = reversed(nums[:])
            return
        key_ex = -1
        for i in range(len(nums) - 1, key, -1):
            if nums[i] > nums[key]:
                key_ex = i
                break
        # print(key_ex)
        nums[key], nums[key_ex] = nums[key_ex], nums[key]
        nums[key + 1:] = reversed(nums[key + 1:])
        return

ans = [2, 3, 1]
Solution().nextPermutation(ans)
print(ans)
