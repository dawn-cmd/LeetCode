from typing import List


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1 = list(reversed(arr1))
        arr2 = list(reversed(arr2))
        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1
        if len(arr2) < len(arr1):
            while len(arr2) < len(arr1):
                arr2.append(0)  
        for i in range(5):
            arr1.append(0) 
            arr2.append(0)
        ans = [0] * len(arr1)
        rest = 0
        for i in range(len(arr1)):
            add = arr1[i] + arr2[i] - rest
            if add >= 2:
                ans[i] = add % 2
                rest = add // 2
                continue
            if add == -1:
                ans[i] = 1
                rest = -1
                continue
            ans[i] = add
            rest = 0
        if rest == -1:
            ans.append(1)
        if rest == 1:
            ans.append(1)
            ans.append(1)
        while len(ans) > 1 and ans[-1] == 0:
            ans.pop()
        return list(reversed(ans))
    
print(Solution().addNegabinary([0], [0]))

