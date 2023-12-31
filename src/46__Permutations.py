from typing import List


class Solution:
    def permute(self, nums: List[int]):
        ans = []

        def dfs(now: List[int]):
            if len(now) == len(nums):
                ans.append(now[:])
                return
            s = set(now)
            for num in nums:
                if num in s:
                    continue
                now.append(num)
                dfs(now)
                now.pop()
                
        dfs([])
        return ans


print(Solution().permute([1, 2, 3]))
