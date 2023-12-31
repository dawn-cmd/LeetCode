#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat) * len(mat[0])
        if n != r * c:
            return mat
        res = [[0] * c for _ in range(r)]
        for i in range(n):
            res[i // c][i % c] = mat[i // len(mat[0])][i % len(mat[0])]
        return res
# @lc code=end
