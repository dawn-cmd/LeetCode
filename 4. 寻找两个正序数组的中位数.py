from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findkth(nums1: List[int], nums2: List[int], k: int, s1: int, s2: int) -> int:
            if k == 1:
                if s1 >= len(nums1):
                    return nums2[s2]
                if s2 >= len(nums2):
                    return nums1[s1]
                return min(nums1[s1], nums2[s2])
            if s1 >= len(nums1):
                return nums2[s2 + k - 1]
            if s2 >= len(nums2):
                return nums1[s1 + k - 1]
            if nums1[min(s1 + k // 2 - 1, len(nums1) - 1)] > nums2[min(s2 + k // 2 - 1, len(nums2) - 1)]:
                return findkth(nums1, nums2, k - min(k // 2, len(nums2) - s2), s1, min(s2 + k // 2, len(nums2)))
            else:
                return findkth(nums1, nums2, k - min(k // 2, len(nums1) - s1), min(s1 + k // 2, len(nums1)), s2)
        
        length = len(nums1) + len(nums2)
        if length % 2 == 1:
            return findkth(nums1, nums2, length // 2 + 1, 0, 0)
        else:
            return sum([findkth(nums1, nums2, k, 0, 0) for k in [length // 2, length // 2 + 1]]) / 2

def main():
    print(Solution().findMedianSortedArrays(nums1 = [4], nums2 = [1, 2, 3, 5, 6]))

if __name__ == "__main__":
    main()