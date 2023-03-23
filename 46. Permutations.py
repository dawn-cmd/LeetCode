from typing import List


class Solution:
    def permute(self, nums: List[int]) -> None:
        ans = []
        
        def dfs(now: List[int]):
            if len(now) == len(nums):
                ans.append(now[:])
            s = set(now)
            for num in nums:
                if num not in s:
                    now.append(num)
                    dfs(now)
                    now.pop()
        
        dfs([])
        
        return ans

print(Solution().permute([1, 2, 3]))
