from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dir = 0
        x = 0
        y = 0
        for _ in range(len(matrix) * len(matrix[0])):
            ans.append(matrix[x][y])
            matrix[x][y] = 0x3f3f3f3f
            nx = x + d[dir][0]
            ny = y + d[dir][1]
            if not (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0])) or matrix[nx][ny] == 0x3f3f3f3f:
                dir = (dir + 1) % 4
                nx = x + d[dir][0]
                ny = y + d[dir][1]
            x = nx
            y = ny
        return ans
