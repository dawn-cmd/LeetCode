from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] = cnt[num] + 1
        f = []
        for key in cnt:
            f.append((key, cnt[key]))
        f.sort(key=lambda x: -x[1])
        ans = [f[i][0] for i in range(k)]
        return ans

print(Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2))
