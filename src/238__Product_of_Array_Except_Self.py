from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multSum = 1
        cntZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                multSum *= nums[i]
            else:
                cntZero += 1
        ans = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            if nums[i] == 0:
                if cntZero == 1:
                    ans[i] = multSum
                else:
                    ans[i] = 0
            else:
                if cntZero > 0:
                    ans[i] = 0
                else:
                    ans[i] = multSum // nums[i]
        return ans

print(Solution().productExceptSelf(nums = [1,2,3,4]))
