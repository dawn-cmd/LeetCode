from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        nums += nums[:l - k]
        for i in range(l - k):
            nums.pop()
