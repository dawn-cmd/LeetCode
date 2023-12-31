from bisect import bisect_left
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        
        def count(mid: int) -> int:
            cnt = 0
            i = 0
            for j, num in enumerate(nums):
                while num - nums[i] > mid:
                    i += 1
                cnt += j - i
            return cnt
        
        return bisect_left(range(nums[-1] - nums[0]), k, key=count)

def main():
    print(Solution().smallestDistancePair(nums = [1,6,1], k = 3))

if __name__ == "__main__":
    main()
