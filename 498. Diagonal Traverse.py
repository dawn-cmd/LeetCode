from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        for layer in range(len(mat) + len(mat[0]) - 1):
            for i in (range(len(mat)) if layer % 2 != 0 else range(len(mat) - 1, -1, -1)):
                j = layer - i
                if not 0 <= j < len(mat[0]):
                    continue
                ans.append(mat[i][j])
        return ans
    
def main():
    print(Solution().findDiagonalOrder(mat = [[1,2,3],[4,5,6],[7,8,9]]))

if __name__ == "__main__":
    main()
