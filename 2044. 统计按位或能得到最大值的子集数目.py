from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_num = 0
        for num in nums:
            max_num |= num

        def dfs(id: int, now: int) -> int:
            if id == len(nums):
                return 1 if now == max_num else 0
            return dfs(id + 1, now) + dfs(id + 1, now | nums[id])
        
        return dfs(0, 0)

def main():
    print(Solution().countMaxOrSubsets(nums = [3,2,1,5]))

if __name__ == "__main__":
    main()