from random import randrange
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums


    def pick(self, target: int) -> int:
        cnt = 0
        ans = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                cnt += 1
                if randrange(cnt) == 0:            
                    ans = i
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
