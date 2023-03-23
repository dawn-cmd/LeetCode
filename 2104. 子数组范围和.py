import sys
from typing import List


class Solution:
    
    def subArrayRanges(self, nums: List[int]) -> int:
        min_num = [[sys.maxsize for _ in range(len(nums))] for _ in range(len(nums))]
        max_num = [[-sys.maxsize for _ in range(len(nums))] for _ in range(len(nums))]
        for l in range(len(nums)):
            for r in range(l, len(nums)):
                if l == r:
                    min_num[l][r] = nums[l]
                    max_num[l][r] = nums[l]
                    continue
                min_num[l][r] = min(min_num[l][r - 1], nums[r])
                max_num[l][r] = max(max_num[l][r - 1], nums[r])
        ans = 0
        for l in range(len(nums)):
            for r in range(l, len(nums)):
                ans += max_num[l][r] - min_num[l][r]
        return ans

def main():
    print(Solution().subArrayRanges(nums = [4,-2,-3,4,1]))       

if __name__ == "__main__":
    main()
