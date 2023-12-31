from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k = len(nums) - 1
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                while nums[i] + nums[j] + nums[k] > 0 and k > j:
                    k -= 1
                if nums[i] + nums[j] + nums[k] == 0 and i != j != k:
                    ans.append([nums[i], nums[j], nums[k]])
        return ans

def main():
    print(Solution().threeSum(nums = [1, 2, -2, -1]))

if __name__ == "__main__":
    main()

