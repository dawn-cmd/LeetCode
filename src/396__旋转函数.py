from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        tot = sum(nums)
        f = [0 for _ in range(len(nums))]
        f[0] = sum([i * nums[i] for i in range(len(nums))])
        for i in range(1, len(nums)):
            f[i] = f[i - 1] + tot - nums[len(nums) - i] * len(nums)
        return max(f)
    
def main():
    print(Solution().maxRotateFunction([4,3,2,6]))

if __name__ == "__main__":
    main()
