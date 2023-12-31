from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [nums[i] for i in range(len(nums)) if nums[i] - 1 != i]

def main():
    print(Solution().findDuplicates(nums = [4,3,2,7,8,2,3,1]))

if __name__ == "__main__":
    main()
