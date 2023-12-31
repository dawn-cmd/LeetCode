from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(max(nums) - min(nums) - 2 * k, 0)

def main():
    print(Solution().smallestRangeI(nums = [1,3,6], k = 3))

if __name__ == "__main__":
    main()
