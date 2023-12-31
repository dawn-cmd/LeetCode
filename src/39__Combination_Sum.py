from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs(now: List[int], id: int, rest: int):
            if rest == 0: return ans.append(now[:])
            if id == len(candidates): return
            dfs(now, id + 1, rest)
            i = 1
            while rest - candidates[id] * i >= 0:
                now.append(candidates[id])
                dfs(now, id + 1, rest - candidates[id] * i)
                i += 1
            while len(now) and now[-1] == candidates[id]:
                now.pop()
        
        dfs([], 0, target)
        return ans

print(Solution().combinationSum([2, 3, 5], 8))
