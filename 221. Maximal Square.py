from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        matrix = [[int(matrix[i][j]) for j in range(len(matrix[i]))] for i in range(len(matrix))]
        presum = [[0 for _ in range(len(matrix[0]))] for __ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                presum[i][j] = matrix[i][j]
                if i > 0:
                    presum[i][j] += presum[i - 1][j]
                if j > 0:
                    presum[i][j] += presum[i][j - 1]
                if i > 0 and j > 0:
                    presum[i][j] -= presum[i - 1][j - 1]
        for length in range(len(matrix), 0, -1):
            for i in range(length - 1, len(matrix)):
                for j in range(length - 1, len(matrix[i])):
                    cnt = presum[i][j]
                    up = i - length + 1
                    left = j - length + 1
                    if up > 0:
                        cnt -= presum[up - 1][j]
                    if left > 0:
                        cnt -= presum[i][left - 1]
                    if up > 0 and left > 0:
                        cnt += presum[up - 1][left - 1]
                    if cnt == length ** 2:
                        return cnt
        return 0
        
print(Solution().maximalSquare(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
