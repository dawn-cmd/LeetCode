from collections import deque
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        q = deque()
        tot = 1
        ans = 0
        for num in nums:
            if tot * num < k:
                q.append(num)
                tot *= num
            else:
                while tot * num >= k and q:
                    ans += len(q)
                    tot //= q.popleft()
                if tot * num < k:
                    q.append(num)
                    tot *= num
        if q:
            ans += sum([i for i in range(1, len(q) + 1)])
        return ans

def main():
    print(Solution().numSubarrayProductLessThanK(nums = [1, 2, 3], k = 0))

if __name__ == "__main__":
    main()
