from collections import Counter
from typing import List


class Solution:

    def countKDifference(self, nums: List[int], k: int) -> int:
        h = Counter()
        cnt = 0
        for i in range(len(nums) - 1, -1, -1):
            cnt += h[nums[i] + k] + h[nums[i] - k]
            h[nums[i]] += 1
        return cnt

def main():
    print(Solution().countKDifference(nums = [3,2,1,5,4], k = 2))

if __name__ == "__main__":
    main()