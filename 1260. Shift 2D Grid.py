from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        convert = []
        for line in grid:
            convert = convert + line
        # print(convert)
        k %= len(convert)
        if k == 0:
            return grid
        convert = convert[-k:] + convert[:-k]
        id = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = convert[id]
                id += 1
        return grid
    
print(Solution().shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))
