from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        now = set()
        for i in range(len(nums)):
            if nums[i] in now:
                return True
            now.add(nums[i])
            if i >= k:
                now.remove(nums[i - k])
        return False

def main():
    solution = Solution()
    print(solution.containsNearbyDuplicate(nums=[1,2,3,1,2,3], k=2))

if __name__ == "__main__":
    main()
