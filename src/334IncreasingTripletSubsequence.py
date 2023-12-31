from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_num = 2 ** 31
        sub_min_num = 2 ** 31
        for num in nums:
            if num <= min_num:
                min_num = num
            elif num <= sub_min_num:
                sub_min_num = num
            else:
                return True
        return False

def main():
    solution = Solution()
    print(solution.increasingTriplet(nums=[2,1,5,0,4,6]))

if __name__ == "__main__":
    main()