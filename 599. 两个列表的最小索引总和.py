import sys
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        min_id = sys.maxsize
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if i + j == min_id:
                        ans.append(list1[i])
                    elif i + j < min_id:
                        min_id = i + j
                        ans = [list1[i]]
        return ans

def main():
    print(Solution().findRestaurant(list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"], list2 = ["KFC", "Shogun", "Burger King"]))

if __name__ == "__main__":
    main()