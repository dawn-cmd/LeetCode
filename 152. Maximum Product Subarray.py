from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cnt = 1
        ans1 = float("-inf")
        for num in nums:
            cnt = cnt * num if cnt else num
            ans1 = max(ans1, cnt)
        cnt = 1
        ans2 = float("-inf")
        for num in nums[::-1]:
            cnt = cnt * num if cnt else num
            ans2 = max(ans2, cnt)
        return max(ans1, ans2)
    
print(Solution().maxProduct(nums = [2,3,-2,4]))
