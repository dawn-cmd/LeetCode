from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = len(matrix) - 1, 0
        n, m = len(matrix), len(matrix[0])
        while 0 <= x < n and 0 <= y < m:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                x -= 1
                continue
            if matrix[x][y] < target:
                y += 1
                continue
        return False

print(Solution().searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5))
