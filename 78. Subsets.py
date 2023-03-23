from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            for i in range(len(ans)):
                tmp = ans[i][:]
                tmp.append(num)
                ans.append(tmp)
        return ans

print(Solution().subsets(nums = [1, 2, 3]))
