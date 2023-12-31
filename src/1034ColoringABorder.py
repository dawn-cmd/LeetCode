from typing import List


class Solution:

    def dfs(self, h: List[List[int]], grid: List[List[int]], x: int, y: int):
        if h[x][y] == 1:
            return
        h[x][y] = 1
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        target = grid[x][y]
        for d in direction:
            if x + d[0] == -1 or x + d[0] == len(grid) or y + d[1] == -1 or y + d[1] == len(grid[0]):
                grid[x][y] = -1
            elif grid[x + d[0]][y + d[1]] == target:
                self.dfs(h, grid, x + d[0], y + d[1])
            elif grid[x + d[0]][y + d[1]] != -1:
                grid[x][y] = -1

    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        h = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        self.dfs(h, grid, row, col)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    grid[i][j] = color
        return grid

def main():
    grid = [[1,1,1],[1,1,1],[1,1,1]]
    row = 2
    col = 1
    color = 2
    test = Solution()
    grid = test.colorBorder(grid, row, col, color)
    print(grid)

if __name__ == "__main__":
    main()

        
