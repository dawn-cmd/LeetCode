from typing import List


class Solution:
    
    def pancakeSort(self, arr: List[int]) -> List[int]:
        final = arr[:]
        final.sort()
        ans = []
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == final[i]:
                continue
            elif arr[0] == final[i]:
                arr[:i + 1] = list(reversed(arr[:i + 1]))
                ans.append(i + 1)
            else:
                id = arr.index(final[i])
                arr[:id + 1] = list(reversed(arr[:id + 1]))
                ans.append(id + 1)
                arr[:i + 1] = list(reversed(arr[:i + 1]))
                ans.append(i + 1)
        return ans

def main():
    print(Solution().pancakeSort([3, 5, 4, 1, 2]))

if __name__ == "__main__":
    main()

