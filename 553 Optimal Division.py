from typing import List


class Solution:

    def optimalDivision(self, nums: List[int]) -> str:
        ans = ""
        for i, num in enumerate(nums):
            if len(nums) > 2 and i == 1:
                ans += '('
            ans += str(num)
            if i == len(nums) - 1:
                if len(nums) > 2:
                    ans += ')'
            else:
                ans += '/'
        return ans

def main():
    print(Solution().optimalDivision([1000,100,10,2]))

if __name__ == "__main__":
    main()