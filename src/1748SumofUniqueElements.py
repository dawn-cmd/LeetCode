from typing import List


class Solution:

    def sumOfUnique(self, nums: List[int]) -> int:
        return sum([x for x in nums if nums.count(x) == 1])

def main():
    print(Solution().sumOfUnique(nums = [1,2,3,2]))

if __name__ == "__main__":
    main()