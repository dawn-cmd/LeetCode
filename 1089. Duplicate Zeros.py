from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        id = 0
        tmp = arr[:]
        while id < len(arr):
            if tmp[id] == 0:
                tmp[id:id] = [0]
                id += 1
            id += 1
        for i, num in enumerate(tmp[:len(arr)]):
            arr[i] = num

print(Solution().duplicateZeros(arr = [1,0,2,3,0,4,5,0]))
