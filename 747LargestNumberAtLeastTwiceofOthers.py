from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = -1
        index = -1
        for i in range(len(nums)):
            if nums[i] > max_num:
                max_num = nums[i]
                index = i
        for i in range(len(nums)):
            if i == index:
                continue
            if max_num < nums[i] * 2:
                return -1
        return index

def main():
    solution = Solution()
    print(solution.dominantIndex(nums = [3,6,1,0]))

if __name__ == "__main__":
    main()