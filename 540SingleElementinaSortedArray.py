from typing import List


class Solution:
    
    def singleNonDuplicate(self, nums: List[int]) -> int:

        def check(id: int) -> int:
            if (id == 0 and nums[id] != nums[id + 1]) or (id == len(nums) - 1 and nums[id] != nums[id - 1]) or (nums[id] != nums[id + 1] and nums[id] != nums[id - 1]):
                return 0
            if id == 0 or nums[id] == nums[id + 1]:
                return -1 if id % 2 == 0 else 1
            if id == len(nums) - 1 or nums[id] == nums[id - 1]:
                return -1 if id % 2 == 1 else 1
        
        st, ed = 0, len(nums) - 1
        while st < ed:
            mid = (st + ed) // 2
            act = check(mid)
            if act == 0:
                return nums[mid]
            if act == -1:
                st = mid + 1
            if act == 1:
                ed = mid - 1
        return nums[st]
    
def main():
    print(Solution().singleNonDuplicate(nums = [1,1,2,3,3,4,4,8,8]))

if __name__ == "__main__":
    main()