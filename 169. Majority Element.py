from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            cnt += 1 if ans == nums[i] else -1
            if cnt == 0:
                ans = nums[i]
                cnt = 1
            # print(ans)
        return ans

print(Solution().majorityElement(nums = [3,2,3]))
