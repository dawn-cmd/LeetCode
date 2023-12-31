from typing import List


class Solution:

    def numEnclaves(self, grid: List[List[int]]) -> int:
        h = set()

        def dfs(x: int, y: int) -> int:
            if (x, y) in h or x < 0 or x >= len(grid) or y < 0 or y >=len(grid[0]) or grid[x][y] == 0:
                return 0
            h.add((x, y))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            return sum([dfs(x + d[0], y + d[1]) for d in directions]) + 1

        cnt = 0
        for i in range(len(grid)):
            if (i, 0) not in h and grid[i][0] == 1:
                cnt += dfs(i, 0)
            if (i, len(grid[0]) - 1) not in h and grid[i][-1] == 1:
                cnt += dfs(i, len(grid[0]) - 1)
        for i in range(len(grid[0])):
            if (0, i) not in h and grid[0][i] == 1:
                cnt += dfs(0, i)
            if (len(grid) - 1, i) not in h and grid[-1][i] == 1:
                cnt += dfs(len(grid) - 1, i)
        return sum([sum([i for i in x]) for x in grid]) - cnt

def main():
    print(Solution().numEnclaves(grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))

if __name__ == "__main__":
    main()