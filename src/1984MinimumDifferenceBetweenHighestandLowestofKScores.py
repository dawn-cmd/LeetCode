from typing import List


class Solution:
    
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min([nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1)])

def main():
    print(Solution().minimumDifference(nums = [9,4,1,7], k = 2))

if __name__ == "__main__":
    main()