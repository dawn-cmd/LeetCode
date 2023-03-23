from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans_l = bisect_left(nums, target)
        ans_r = bisect_right(nums, target)
        if not 0 <= ans_l < len(nums) or nums[ans_l] != target:
            return [-1, -1]
        else:
            return [ans_l, ans_r - 1]

print(Solution().searchRange([2, 2], 3))
